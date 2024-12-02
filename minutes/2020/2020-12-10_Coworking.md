# HPCC Coworking Hours: 10 December

The HPC Carpentries Task Force holds coworking hours every other Thursday, with
two time slots intended to provide adequate coverage for our global
constituency. Check your local times below, and join whichever is most
convenient. See you soon!

<!-- Important links to define, placed up top for convenience -->

[earlier]:
  https://www.timeanddate.com/worldclock/fixedtime.html?iso=20201210T1200&msg=HPC+Carpentries+Coworking+Hour+1
[evening]:
  https://www.timeanddate.com/worldclock/fixedtime.html?iso=20201210T2200&msg=HPC+Carpentries+Coworking+Hour+2
[last-cowork]: https://codimd.carpentries.org/m7WTG6EYR82AlhbYZnWJ5g?view
[last-coord]: https://codimd.carpentries.org/tsMOzEaMQYmeesMGpalVRw?view

#### Check your local times

These two meeting times provide the least-painful coverage for the six
non-polar continents. Folks in Antarctica and aboard a space station are
invited to join whichever is most convenient 😉

- [12:00 UTC][earlier] &mdash; better for Africa, Asia, and Europe
- [22:00 UTC][evening] &mdash; better for the Americas and Australia

#### Slack Video

The meetings will be held, with audio & optional video, through the
`#hpc-carpentry` channel on The Carpentries' Slack. To join Slack, click [this
link][invite]. If you have already joined, login through [this link][slack].

#### Backtrace

Notes from the previous Coworking Hour are [here][last-cowork].

Notes from the previous Coordination Meeting are [here][last-coord].

---

## Earlier Meeting (Africa, Asia, and Europe)

### Participants

- _name (pronouns), interests_
- Benson Muite, PGAS languages, HPC education, Efficiency
- Alan O'Cais (he/him), HPC Education, Software availability and efficiency

### Agenda & Notes

- New website repository: <https://github.com/hpc-carpentry/hpc-carpentry.org>

  - Did everything transfer?
    - [Update on this in the associated issue](https://github.com/hpc-carpentry/hpc-carpentry.org/issues/5#issuecomment-742532227)
  - Deprecation warning in old repo?
    - [Suggested the mechanics for how to do this](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/29#issuecomment-742497646)

- Progress on artwork &rarr;
  [awesome options from @annajiat's students](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/28).
  Leaderboard as of 1 December:

  1. [Design 5](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/28#issuecomment-729230704)
     by Mumtahinah Sristy
  2. [Design 4](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/28#issuecomment-729229992)
     by Md Sabbir al Mamon
  3. [Design 7](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/28#issuecomment-729231597)
     by Sakib Hassan

- Start reviewing older issues to see whether they've been addressed, and
  consolidating the open ones.

  - Update to shell lesson proposed
  - Cleaned out or transferred issues in
    https://github.com/hpc-carpentry/hpc-carpentry.github.io
    - There was some useful evaluation forms in there!

- Discuss linux for HPC

---

## Later Meeting (Americas & Australia)

### Participants

- _name (pronouns), affiliation, interests_
- Andrew Reid (he/him), NIST, frictionless HPC for everyone!
- Trevor Keller (he/him, they/them), NIST Center for Theoretical &
  Computational Materials Science, speed & I/O
- Mark Piercy, Stanford

### Agenda & Notes

- New website repository: <https://github.com/hpc-carpentry/hpc-carpentry.org>

  - The new website builds locally for Andrew & Trevor. Rejoice!
  - Did everything transfer?
  - From the earlier session,
    [update on this in the associated issue](https://github.com/hpc-carpentry/hpc-carpentry.org/issues/5#issuecomment-742532227).
    - [ ] https://hpc-carpentry.github.io/workshops
    - [ ] https://hpc-carpentry.github.io/why-hpc-carpentry
    - [ ] https://hpc-carpentry.github.io/about
    - [ ] https://hpc-carpentry.github.io/our-lessons (this actually exists but
          we need to figure out how to sync the content )
  - Deprecation warning in old repo?
    - From the earlier session,
      [suggested the mechanics for how to do this](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/29#issuecomment-742497646).

- Progress on artwork &rarr;
  [awesome options from @annajiat's students](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/28).
  Leaderboard as of 1 December:

  1. [Design 5](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/28#issuecomment-729230704)
     by Mumtahinah Sristy
  2. [Design 4](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/28#issuecomment-729229992)
     by Md Sabbir al Mamon
  3. [Design 7](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/28#issuecomment-729231597)
     by Sakib Hassan

- Start reviewing older issues to see whether they've been addressed, and
  consolidating the open ones.

- Mark Piercy has been teaching an old version ~ once per quarter; attracts
  HPC-curious crowd.
  - He likes the new Intro to MPI material.
  - The simple examples (`pi.c`, stolen from the Debian MPI example) are nice.
  - The new `rsync` examples are good, more useful than `sftp`.
  - Hands-on with Sherlock cluster. Harder now we're remote, since the course
    is hands-on, and it's much harder to see what's going on for the learners
    over VTC than it is f2f.
    - https://shellshare.net/
  - Spends about half the course on profiling & monitoring. Helpful to have
    learners run a long job, use `sacct` to find the node it's running on, SSH
    to it, and run `htop` so they can see it's using very little memory, one
    core, etc.
  - Remind users the queue is a moving target: it may look bad for a while, but
    suddenly a big job will end and everything moves.
  - Request as little as possible to improve your odds of launching sooner.
    Might sneak in ahead of other people.
  - Some folks using `snakemake` for more complex workflows & job dependencies
    than Slurm's job arrays.
    - Learners are impressed by the force-multiplication of clusters: a set of
      300 similar jobs will go 1 or 2 at a time on your laptop, but could all
      run at once on the cluster.
  - A small group of users are MPI-aware and use massive resources (physics,
    cosmology, materials, chem). Roughly 10:1 are very small jobs, but in very
    large numbers (bio-informatics).
  - Using [OpenOnDemand](https://openondemand.org). "File editor" is a WYSIWYG
    browser tool with drag-and-drop; helpful for folks unfamiliar with
    command-line editors.
    - Actual dispatch of jobs to the cluster ("job composer") is the worst.
      Nominally generates an SBATCH file somewhere, but totally opaque &
      inaccessible. Much easier to open a shell & editor, write the script
      yourself.
    - JupyterLab & TensorBoard interfaces are pretty handy.
    - Prereq: OpenVNC on each compute node. Without it, OOD is much less smooth
      and can be less stable.

---

General questions or feedback? Contact <team@carpentries.org>.

<!--References-->

[conduct]:
  https://docs.carpentries.org/topic_folders/policies/code-of-conduct.html
[invite]: https://swc-slack-invite.herokuapp.com/
[license]: https://creativecommons.org/licenses/by/4.0/
[slack]: https://swcarpentry.slack.com
