# HPCC Coworking Hours: 6 May 2021

The HPC Carpentries Task Force holds coworking hours on the first Thursday,
with two time slots intended to provide adequate coverage for our global
constituency. Check your local times below, and join whichever is most 
convenient. A Google calendar has been set up to capture these events, 
available [online][gcal] or as an [ical file][ical]. 

See you soon!

<!-- Important links to define, placed up top for convenience -->
[earlier]: https://www.timeanddate.com/worldclock/fixedtime.html?iso=20210506T1200&msg=HPC+Carpentries+Coworking+Hour+1
[evening]: https://www.timeanddate.com/worldclock/fixedtime.html?iso=20210506T2200&msg=HPC+Carpentries+Coworking+Hour+2
[last-cowork]: https://codimd.carpentries.org/dHcLlDZnQ_6UvEUd76f2-Q?view
[last-coord]: https://codimd.carpentries.org/yxz3pFqJS_Wx_DLmHR49wQ?view

#### Check your local times

These two meeting times provide the least-painful coverage for the six
non-polar continents. Folks in Antarctica and aboard a space station
are invited to join whichever is most convenient 😉

* [12:00 UTC][earlier] &mdash; better for Africa, Asia, and Europe
* [22:00 UTC][evening] &mdash; better for the Americas and Oceania

### Virtual Venue

Both meetings will use Google Meet.

### Callbacks to Previous Meetings

- [Previous Coworking Hour][last-cowork]
- [Previous Coordination Meeting][last-coord]
- Archive of old [Minutes][minutes]

---

## Earlier Meeting (Africa, Asia, and Europe)

### Participants

* Trevor Keller (they/them), NIST
* Andrew Reid (he/him), NIST
* Benson Muite
* Callum Walley (they/any), NeSI

### Agenda & Minutes

Merged PR#346 on the hpc-intro lesson, about `wget` or `curl` for downloading.

Discussion about the parallel example. Benson is interested in what's available
in Alan's software stack, with a view to getting parallel example codes for
other languages, especially R, but also Spark (cloud-centric alternative to
Slurm).

The general scheme is, there are communities, especially Spark, where learners
already know how to do interesting and useful use-cases on local machines, e.g.
R, DeapSecure, Spark communities. We can add value to these communities by
creating a pathway to using clusters, the main barrier we need to get them over
is job submission. The benefit to our content is that these tools typically get
you to more modern and interesting use-cases than the standard MPI use-cases.

* "Modern and interesting" meaning data-centric, machine learning type, like
  map-reduce. The benefit of this is that many learners will be motivated to
  engage with these topics. This is "hotness".

The first lesson should be common to "HPC" and "Machine Learning" communities.
Everybody needs to know how to log in & transfer files. Beyond that, the
communities diverge in toolsets/frameworks. Let DeapSecure & relatives teach to
those folks, rather than developing AI/ML/Cloud lessons ourselves? Or, consider
developing

* Spark lesson
* Dask lesson

<i class="fa fa-user" aria-hidden="true"></i> Benson shared candidate Python
code (incorporating suggestions from Lisandro Dalcin)

```python
import numpy as np
import sys
import datetime
from mpi4py import MPI

def inside_circle(total_count):
  x = np.random.uniform(size=total_count)
  y = np.random.uniform(size=total_count)
  radii = np.sqrt(x*x + y*y)
  count = len (radii[np.where(radii<=1.0)])
  return count

def main():
  comm = MPI.COMM_WORLD
  size = comm.Get_size()
  rank = comm.Get_rank()
  n_samples = int(sys.argv[1])
  my_samples = n_samples//size + ( N % size > rank)

  my_start_time = MPI.Wtime()
  my_counts = inside_circle(my_samples)
  counts = comm.reduce(my_counts,op=MPI.SUM,root=0)
  my_end_time = MPI.Wtime()
  my_elapsed_time = my_end_time - my_start_time
  max_elapsed_time = comm.reduce(my_elapsed_time,op=MPI.MAX,root=0)
  my_pi = 4.0 * counts / n_samples
  if rank == 0:
    print("Pi: {}, time: {} s".format(my_pi,max_elapsed_time))

if __name__ == '__main__':
  main()

```

Consensus is that the arithmetic for "my_samples" is too much at once, should
be broken out into bite-sized steps for learners. Otherwise, this is good
parallel example code. Update diagrams.

#### UTC vs DST

Since our calendar goes by UTC, the relative time of this meeting has shifted
by one hour where Daylight Saving Time is in effect. This has created at least
one clash

---

## Later Meeting (Americas & Australia)

### Participants

* Andrew Reid (he/him), NIST
* Trevor Keller (they/them), NIST
* Mike Renfro, TN Tech
* Callum Walley (presumed human), NeSI

### Agenda & Minutes

Early discussion about the hpc-shell lesson, which is of interest to Callum
Walley. The operational question of whether we want to use a fully local
hpc-shell lesson, use the Carpentries' bash-novice and supplement it. The
advantage of re-using Carpentries' content is that we automatically get
improvements from the community, but there is operational convenience in being
able to point to one thing that's easy for leaners to consume.

The hpc-shell lesson is also a good place for HPC-specific shell issues like
the difference between file systems, protected vs unprotected, local vs.
remote, high vs. low performance, and so forth.

Possible re-factoring proposal: Maybe hpc-intro should be a single-unit (30 to
60 minutes) that explains how clusters work, and then tails into something like
hpc-shell with operational details of SSH, and then finishes.

Additional issue: HPC-shell has a lot of options for tools to use to get to a
command-line prompt, this is potentially confusing, especially on Windows,
where there's MobaXterm, WSL, puTTY, and GitBash. Can we use the templating
schemes to hide some of these options? Is that in scope for customization, or
should institutions that want to do that fork?

---

*Want to embed a "user" icon, as in `[name=Name]`?* Embed this 
`<i class="fa fa-user" aria-hidden="true">Name</i>` to get this: <i class="fa fa-user" aria-hidden="true"> Name</i>

<!--HPC Carpentry References-->
[coordination]: https://github.com/hpc-carpentry/coordination
[gcal]: https://calendar.google.com/calendar/?cid=bWp0ZWh0ZmEycmVjZGZtNmZjdGUwMWVhdGNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ
[ical]: https://calendar.google.com/calendar/ical/mjtehtfa2recdfm6fcte01eatc%40group.calendar.google.com/public/basic.ics
[minutes]: https://github.com/hpc-carpentry/coordination/tree/main/minutes
[website]: https://github.com/hpc-carpentry/hpc-carpentry.github.io

[hpc-chapel]: https://github.com/hpc-carpentry/hpc-chapel
[hpc-intro]: https://github.com/carpentries-incubator/hpc-intro
[hpc-parallel]: https://github.com/hpc-carpentry/hpc-parallel-novice
[hpc-python]: https://github.com/hpc-carpentry/hpc-python
[hpc-shell]: https://github.com/hpc-carpentry/hpc-shell

<!--Carpentries References-->
[conduct]: https://docs.carpentries.org/topic_folders/policies/code-of-conduct.html
[invite]: https://swc-slack-invite.herokuapp.com/
[license]: https://creativecommons.org/licenses/by/4.0/
[slack]: https://swcarpentry.slack.com
