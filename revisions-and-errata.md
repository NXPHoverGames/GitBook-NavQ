# Revisions and Errata

## Fault\_N on USB C chips

| Board    | Rev    | Item                                                                                 |
| -------- | ------ | ------------------------------------------------------------------------------------ |
| RDDRONE- | HGI-1A | <p>PTN5110 FAULT_N should be pulled up</p><p>and connected to INT of NX20P4383UK</p> |

**Action** - Mask this interrupt in the register FAULT\_STATUS\_MASK (0x15h):bit 4 -- Force Discharge Failed Interrupt Status Mask (to be zeroed).

Resolve in the software, since both the PTN5110 (TCPC) and NX20P3483 (power switch) connected to the I2C bus.\
Polling of the NX20P3483 will address this errata.

This issue will be resolved in the next board revision (RDDRONE-HGI-2A)

## SD 3.0 Power Switch is missing

| Board    | Rev      | Item                                                                 |
| -------- | -------- | -------------------------------------------------------------------- |
| RDDRONE- | MEDIA-1A | The design is missing a power switch required by the SD 3.0 standard |

**Action** - disable SD3.0 support in UBoot and/or avoid SD3.0 cards&#x20;

This issue will be resolved in the next board revision (RDDRONE-MEDIABOARD-2A)

The SD3.0 PWR switch will be added:

![](<.gitbook/assets/image (29).png>)

## 3rd Mounting hole on carbon fiber plate

**Issue** - The 3rd mounting hole for the NavQ was missed on the carbon fiber mounting plate.  This is needed to secure the board and avoid vibrations.

**Action** - Please drill a 3mm hole manually or use double sided tape on this side of the baord mounting. This must be done to avoid vibration of the board during flight.&#x20;



