# The world is a prison for the believer.

from django.dispatch import Signal

## This event is fired before CodexPanel core load template for create backup page.
preBackupSite = Signal()

## This event is fired after CodexPanel core load template for create backup page.
postBackupSite = Signal()

## This event is fired before CodexPanel core load template for restore backup page.
preRestoreSite = Signal()

## This event is fired after CodexPanel core load template for restore backup page.
postRestoreSite = Signal()

## This event is fired before CodexPanel core start creating backup of a website
preSubmitBackupCreation = Signal()

## This event is fired before CodexPanel core starts to load status of backup started earlier througb submitBackupCreation
preBackupStatus = Signal()

## This event is fired after CodexPanel core has loaded backup status
postBackupStatus = Signal()

## This event is fired before CodexPanel core start deletion of a backup
preDeleteBackup = Signal()

## This event is fired after CodexPanel core finished the backup deletion
postDeleteBackup = Signal()

## This event is fired before CodexPanel core start restoring a backup.
preSubmitRestore = Signal()

## This event is fired before CodexPanel core starts to add a remote backup destination
preSubmitDestinationCreation = Signal()

## This event is fired after CodexPanel core is finished adding remote backup destination
postSubmitDestinationCreation = Signal()

## This event is fired before CodexPanel core starts to delete a backup destination
preDeleteDestination = Signal()

## This event is fired after CodexPanel core finished deleting a backup destination
postDeleteDestination = Signal()

## This event is fired before CodexPanel core start adding a backup schedule
preSubmitBackupSchedule = Signal()

## This event is fired after CodexPanel core finished adding a backup schedule
postSubmitBackupSchedule = Signal()

## This event is fired before CodexPanel core start the deletion of backup schedule
preScheduleDelete = Signal()

## This event is fired after CodexPanel core finished the deletion of backup schedule
postScheduleDelete = Signal()

## This event is fired before CodexPanel core star the remote backup process
preSubmitRemoteBackups = Signal()

## This event is fired after CodexPanel core finished remote backup process
postSubmitRemoteBackups = Signal()

## This event is fired before CodexPanel core star the remote backup process
preStarRemoteTransfer = Signal()

## This event is fired after CodexPanel core finished remote backup process
postStarRemoteTransfer = Signal()

## This event is fired before CodexPanel core start restore of remote backups
preRemoteBackupRestore = Signal()

## This event is fired after CodexPanel core finished restoring remote backups in local server
postRemoteBackupRestore = Signal()
