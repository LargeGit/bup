"""
Protection Policy Object
    ID
    Type {WRITE|READ|COPY|DELETE}
    target device
        DUT
        {PRIMARY|SECONDARY share/store}
    data source 
        size
        change rate
    protection schedule
    settings
        retries
"""

"""
Device configuration Object
    ID
    type {VT|NAS|CATALYST}
    DUT
    target
    settings
"""

"""
Data Job object
    ID
    type {WRITE|READ|COPY|DELETE|PAUSE|CANCEL}
    status {QUEUED|RUNNING|CANCELLED|PAUSED}
    target device
    target share
    data source info
    settings
"""

"""
Catalog entry
    ID
    type {WRITE|READ|COPY|DELETE}
    target device
    target share
    data source info
    settings
"""