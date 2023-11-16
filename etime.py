import ntptime
import time


def ntp_settime():
    def try_ntp(num_trials):
        for i in range(num_trials):
            try:
                ntptime.settime()
                return i
            except OSError:
                time.sleep(1)
        else:
            raise OSError('NTP time sync failed after {} trials'.format(num_trials)) 

    trials = try_ntp(10)
    print('NTP time synchronization succeeded with {} trials: {}'.format(trials, format_utctime()))


# TODO: Support local time.
def format_utctime():
    t = time.gmtime()
    return '{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}'.format(
        year=t[0], month=t[1], day=t[2], hour=t[3], minute=t[4], second=t[5])