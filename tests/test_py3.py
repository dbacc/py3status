from py3status.py3 import Py3


def test_format_units():

    tests = [
        # basic unit guessing
        (dict(value=100), (100, 'B')),
        (dict(value=999), (999, 'B')),
        (dict(value=1000), (0.977, 'KiB')),
        (dict(value=1024), (1.0, 'KiB')),
        (dict(value=pow(1024, 2)), (1.0, 'MiB')),
        (dict(value=pow(1024, 3)), (1.0, 'GiB')),
        (dict(value=pow(1024, 4)), (1.0, 'TiB')),
        (dict(value=pow(1024, 5)), (1.0, 'PiB')),

        # no guessing
        (dict(value=pow(1024, 2), auto=False), (pow(1024, 2), 'B')),
        (dict(value=pow(1024, 2), auto=False, unit='B'), (pow(1024, 2), 'B')),
        (dict(value=pow(1024, 2), auto=False, unit='KiB'), (1024, 'KiB')),

        # guess with si units
        (dict(value=100, si=True), (100, 'B')),
        (dict(value=1000, si=True), (1.0, 'kB')),
        (dict(value=pow(1000, 2), si=True), (1.0, 'MB')),
        (dict(value=pow(1000, 3), si=True), (1.0, 'GB')),
        (dict(value=pow(1000, 4), si=True), (1.0, 'TB')),
        (dict(value=pow(1000, 5), si=True), (1.0, 'PB')),

        # forced MiB
        (dict(value=pow(1024, 1), unit='MiB'), (0.000977, 'MiB')),
        (dict(value=pow(1024, 2), unit='MiB'), (1.0, 'MiB')),
        (dict(value=pow(1024, 3), unit='MiB'), (1024, 'MiB')),
        (dict(value=pow(1024, 4), unit='MiB'), (pow(1024, 2), 'MiB')),
        (dict(value=pow(1024, 5), unit='MiB'), (pow(1024, 3), 'MiB')),

        # endings
        (dict(value=100, unit='b/s'), (100, 'b/s')),
        (dict(value=1024, unit='b/s'), (1.0, 'Kib/s')),
        (dict(value=pow(1024, 2), unit='b/s'), (1.0, 'Mib/s')),
        (dict(value=pow(1000, 2), si=True, unit='b/s'), (1.0, 'Mb/s')),
        (dict(value=pow(1024, 3), unit='Mib/sec'), (1024, 'Mib/sec')),

        # optimal
        (dict(value=1234567890), (1.15, 'GiB')),
        (dict(value=1234567890, optimal=None), (1.1497809458523989, 'GiB')),
        (dict(value=1234567890, optimal=1), (1, 'GiB')),
        (dict(value=1234567890, optimal=2), (1, 'GiB')),
        (dict(value=1234567890, optimal=3), (1.1, 'GiB')),
        (dict(value=1234567890, optimal=5), (1.15, 'GiB')),
        (dict(value=1234567890, unit='MiB'),
            (1177, 'MiB')),
        (dict(value=1234567890, unit='MiB', optimal=None),
            (1177.3756885528564, 'MiB')),
        (dict(value=1234567890, unit='MiB', optimal=2),
            (1177, 'MiB')),
        (dict(value=1234567890, unit='MiB', optimal=6),
            (1177.4, 'MiB')),
        (dict(value=1234567890, unit='MiB', optimal=9),
            (1177.3757, 'MiB')),
    ]

    py3 = Py3()

    for test in tests:
        print(test)
        # we use repr in the assert to ensure 1 and 1.0 are not treated the
        # same
        assert repr(py3.format_units(**test[0])) == repr(test[1])
