# Testing the Meltdown Attack 

1. Preparation
   * Check whether you have a processor that is vulnerable to Meltdown:
     * [Intel][1]
     * [AMD][2]
     * [ARM][3]
   * Download and install the [Verifiable Builds][4] of [Meltdown Checker][5]

2. Test
   * Run the Meltdown Checker:

```shell
$ ./meltdown_checker.py
```

   * If your processor is vulnerable to Meltdown attack, you'll get an output that looks like this:

```shell
System check (hardware & OS version) ....................... [OK]

Checking for vulnerability to Meltdown attack ............... VULNERABLE
```

   *  If your processor is not vulnerable to Meltdown attack, you'll get an output that looks like this:

```shell
System check (hardware & OS version) ....................... [OK]

Checking for vulnerability to Meltdown attack ............... NOT VULNERABLE
```

[1]: https://www.intel.com/content/www/us/en/support/articles/000005473/processors.html
[2]: https://www.amd.com/en/corporate/speculative-execution
[3]: https://developer.arm.com/support/security-update
[4]: https://github.com/speed47/spectre-meltdown-checker#instructions-verifiable-build
[5]: https://github.com/speed47/spectre-meltdown-checker

## Testing Tools: 

Target Testing   | Testing Technique | Test Analysis  | Test Method | Test Tool        | Mobile Platform
---------------- | ---------------- | ------------- | ---------- | --------------- | --------------
Meltdown Attack | White-box       | Dynamic       | Penetration | Metasploit      | iOS/Android
                | Grey-box        | Static        | Code review | Veracode       | iOS/Android
                | Black-box       | Hybrid        | Fuzz Testing| InsightVM       | iOS/Android 
                |                 |               |            | Burp Suite      | iOS/Android