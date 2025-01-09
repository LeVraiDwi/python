import time
import shutil


def format_time(seconds):
    """
    Format the given time in seconds as MM:SS.
    """
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def format_it(itPerSecond):
    """Return the given time in Git Mit or it per seconde"""
    if itPerSecond / 1000000 > 1:
        return f'{itPerSecond / 1000000:4.4}Git/s'
    elif itPerSecond / 1000 > 1:
        return f'{itPerSecond / 1000:4.4}Mit/s'
    else:
        return f'{itPerSecond:6.4}it/s'


def ft_tqdm(lst: range):
    """    Decorate an iterable object, returning an iterator\
          which acts exactly
    like the original iterable, but prints \
        a dynamically updating
    progressbar every time a value is requested."""

    try:
        assert len(lst) < 9223372036854775808, 'AssertionError: \
            To many element in lst'
        assert type(lst) is range, 'AssertionError:\
            lst must be a range of integer'
        # n = sum(1 for c in lst if type(c) is not int)
    except AssertionError as msg:
        print(msg)
        return

    total = len(lst)

    lenOfTotal = len(str(total))
    barsize = shutil.get_terminal_size().columns - (7 + (lenOfTotal * 2) + 27)
    start = time.time()

    for i in range(1, len(lst) + 1):
        actualTime = time.time() - start
        formatActualTime = format_time(actualTime)
        percent = round(i / total * 100)
        speed = i / actualTime
        eta = (total - i) / speed
        formatEta = format_time(eta)
        actualBarSize = round(i / total * barsize)
        bar = f"{'█' * actualBarSize}{' ' * (barsize - actualBarSize)}"
        backslash = '\r'
        speedTimeStr = f"[{formatActualTime}<{formatEta}, {format_it(speed)}]"
        substr = f"{i:{lenOfTotal}}/{total} {speedTimeStr}"
        percentstr = f"{backslash if i > 1 else ''}{percent:3}%"
        print(f"{percentstr}|{bar}| {substr}", end="", flush=True)
        if i == len(lst):
            print('\n')
        yield
