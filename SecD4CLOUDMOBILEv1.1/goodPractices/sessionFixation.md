# Session Fixation Attack

An attacker has a valid session ID and forces the victim to use this ID.


## Definition

Session Fixation is an attack in which the victim is tricked into using a SID value that is controlled, and thus known, by the attacker. This can be achieved either by supplying a crafted URL including this SID as a parameter to the victim (in case that the vulnerable Web application accepts parameter-based SIDs) or by finding a way to set a copy of this SID cookie to the victim’s browser.

## Attacker Powers

 * Steal SID and access otherwise restricted resources utilizing the victim’s authorization context.
 
 
## Session Fixation Attack Diagram


