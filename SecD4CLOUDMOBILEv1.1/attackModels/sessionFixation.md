# Session Fixation Attack

An attacker has a valid session ID and forces the victim to use this ID.


## Definition

The session fixation attack occurs whenever the victim is induced to use a controlled SID value, that is, known to the attacker. In addition, this can be done in two different ways - setting a copy of that SID cookie to the victim's browser or providing a URL created by including this SID as a parameter for the victim (in case a vulnerable web application accepts parameter-based SIDs).

## Technical Impact
* Gain Privileges or Assume Identity.

## Risk Analysis
* Medium Risk.

## Likelihood of Exploit
* Low.

## Attacker Powers

 * Steal SID and access otherwise restricted resources utilizing the victim’s authorization context.
 
 
## Session Fixation Attack Diagram


