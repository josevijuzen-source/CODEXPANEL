# The world is a prison for the believer.

from django.dispatch import Signal

## This event is fired before CodexPanel core start creation of NS Records.
preNSCreation = Signal()

## This event is fired after CodexPanel core finished creation NS Records.
postNSCreation = Signal()

## This event is fired before CodexPanel core start creation DNS Zone.
preZoneCreation = Signal()

## This event is fired after CodexPanel core finished creation of DNS Zone.
postZoneCreation = Signal()

## This event is fired before CodexPanel core start to add an DNS record.
preAddDNSRecord = Signal()

## This event is fired after CodexPanel core finished adding DNS record.
postAddDNSRecord = Signal()

## This event is fired before CodexPanel core start deletion of DNS Record.
preDeleteDNSRecord = Signal()

## This event is fired after CodexPanel core finished deletion DNS Record.
postDeleteDNSRecord = Signal()

## This event is fired before CodexPanel core start deletion of a DNS Zone.
preSubmitZoneDeletion = Signal()

## This event is fired after CodexPanel core finished deletion of DNS Zone.
postSubmitZoneDeletion = Signal()