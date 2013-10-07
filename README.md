damnwait
========
From the pronunciation it sounds like an app for dmv, and yes it is. This app can provide real-time and statistical data of the wait times of DMV locations, so that you can choose the best slot, this is espacially useful when an appointment is not made in advance.

Technical Details
=================
Backend: a daemon run periodically to pull data from DMV website of the wait times of dmv locations, data will be stored in xml format, and ready to be XQueried.
Frontend: data will be processed from several options per users' request 
1) real time wait time
2) accumulative data of each weekdays (Mon, Tue, Wed, etc)

For these two options, user can choose the time of data gathering start time, e.g. wait time of the past three days, wait time in Monday of the past one year



