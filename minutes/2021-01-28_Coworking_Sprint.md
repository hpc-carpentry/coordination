# HPCC Coworking Hours: 28 January 2021

The HPC Carpentries Task Force holds coworking hours every other Thursday,
with two time slots intended to provide adequate coverage for our global
constituency. Check your local times below, and join whichever is most 
convenient. See you soon!

<!-- Important links to define, placed up top for convenience -->
[earlier]: https://www.timeanddate.com/worldclock/fixedtime.html?iso=20210128T1200&msg=HPC+Carpentries+Coworking+Hour+1
[evening]: https://www.timeanddate.com/worldclock/fixedtime.html?iso=20210128T2200&msg=HPC+Carpentries+Coworking+Hour+2
[last-cowork]: https://codimd.carpentries.org/Kk5G93h9QE6q2wXFbLdG5Q?view
[last-coord]: https://codimd.carpentries.org/j7wbzKFhRpKB8xgJKbyorg?view

#### Check your local times

These two meeting times provide the least-painful coverage for the six
non-polar continents. Folks in Antarctica and aboard a space station
are invited to join whichever is most convenient 😉

* [11:00 UTC](https://www.timeanddate.com/worldclock/fixedtime.html?iso=20210128T1100&msg=LearnHPC+Alan+YouTube) &mdash; Alan will be delivering a 15-minute talk on [LearnHPC](https://easybuild.io/eum/#learnhpc) at the 6th EasyBuild User Meeting. Catch the [livestream](https://www.youtube.com/watch?v=KyDHzxlwJUw&list=PLhnGtSmEGEQh0pCtmkFQsDzeoo6tbYnyZ&index=20)!
* [12:00 UTC][earlier] &mdash; better for Africa, Asia, and Europe
* [22:00 UTC][evening] &mdash; better for the Americas and Australia

### Video Venue

Both meetings will use ~redacted~, updated 21 January with a new URL. 


### Callbacks to Previous Meetings

- [Previous Coworking Hour][last-cowork]
- [Previous Coordination Meeting][last-coord]

---

## Earlier Meeting (Africa, Asia, and Europe)

During this two-hour sprint, we will go through the open issues and PRs on [hpc-intro](https://github.com/carpentries-incubator/hpc-intro), triaging and assigning appropriate labels. The goal at the end of the day is to have a set of actionable issues and pull requests, so we can focus our efforts. 

### Participants

* Toby Hodges (I will join for the start and try to stay as long as possible but might struggle to commit two full hours)
* Benson Muite
* Apologies from Alan, organising the [EasyBuild User Meeting](https://easybuild.io/eum/) and [speaking on LearnHPC](https://easybuild.io/eum/#learnhpc) at 11am UTC
* Andrew Reid, NIST

### Notes

* Catch the [livestream](https://www.youtube.com/watch?v=KyDHzxlwJUw&list=PLhnGtSmEGEQh0pCtmkFQsDzeoo6tbYnyZ&index=20) of Alan's talk at [11:00 to 11:15 UTC](https://www.timeanddate.com/worldclock/fixedtime.html?iso=20210128T1100&msg=LearnHPC+Alan+YouTube)!
* Consider having lessons for example applications such as Fire Dynamics Simulator https://pages.nist.gov/fds-smv/, OOF2 https://www.ctcms.nist.gov/oof/
* [#7](https://github.com/carpentries-incubator/hpc-intro/issues/7), add learner profiles -- this is a good idea, but needs some context, like a better-titled subsection. The advantage is that learners can see themselves in the profiles, to help motiviate participation in the lesson.
    - Trevor: This issue proposes adding three user profiles. Peter suggested  three blurbs, and I committed revised versions some time ago. The discussion of revisions, while useful, is out of scope, as the Issue has been resolved.
* [#9](https://github.com/carpentries-incubator/hpc-intro/issues/9), episode renumbering -- this is superseded by [#230](https://github.com/carpentries-incubator/hpc-intro/issues/230). Closed with a comment to that effect.
* [#228](https://github.com/carpentries-incubator/hpc-intro/issues/228), add this to the Carpentry "help wanted" -- now that we are Carpentries-hosted, we can do this, but maybe wait for the clean-up of legacy issues first to reduce confusion among new-comers to the repo. 
    - Useful info from Toby: The "help wanted" page only lists issues with the "help wanted" tag, broken out by repo, so the danger of confusion is reduced compared to a novice hitting the full repo.
* [#14](https://github.com/carpentries-incubator/hpc-intro/issues/14), define "job" -- identified a good location for this, concur that this should happen.
    - Trevor added Help Wanted and Good First Issue labels. 
* [#15](https://github.com/carpentries-incubator/hpc-intro/issues/15), "Why" of a cluster is missing -- possibly addressed? The "Why use a cluster" lesson covers scenarios where scaling up is needed and a cluster does this.
    - Trevor: Christina addressed this in [#17](https://github.com/carpentries-incubator/hpc-intro/pull/17), adding motivation at the start. This issue is resolved.
* [#18](https://github.com/carpentries-incubator/hpc-intro/issues/18), distinguish between `-n` and `-N` in Slurm. Queuing system variants are covered by the new snippets scheme, and the lesson already uses `-n` and `-N` differently. Verify other queuing system snippets work correctly, and close.
    - Trevor: This is a Slurm  specific thing, and the snippet mechanism works. The issue is resolved.
* [#21](https://github.com/carpentries-incubator/hpc-intro/issues/21), use GNU parallel. Added a link to an existing lesson that uses this as potential useful input. Maybe in a different scope, like a shell-centric lesson? The step up from serial shell to GNU parallel is much lower than going straight to MPI.
    * This issue triggered a very broad discussion on the appropriate scope and the problems surrounding parallelism. On the one hand, MPI is ubiquitous in cluster computing, and is a very high value target to reach in an HPC-intro lesson, which maybe the only HPC lesson a learner ever encounters, so it would be a dis-service to these learners not to get to MPI. The complications of C compilation and the opaqueness of the cpi example code are liabilities, but there is a Python MPI example under consideration. The counterpoint is that MPI is hard to understand and "magic" in a bad way, and GNU parallel introduces the parallelism that is relevant to achieving performance increases. In this second view, MPI content could be deferred to a second lesson, where there would be sufficient time to introduce the necessary background, so it can be omitted form hpc-intro.
    * This is related to the issue of requiring and building on the shell-intro lesson, rather than having a separate hpc-shell lesson. There could then be two HPC lessons, hpc-intro and hpc-advanced, with MPI in the latter section.
    * There are lots of parallel programming models, and there is content out there we can use as a resource for a secondary lesson, e.g. Chapel, [UPC++](https://upcxx.lbl.gov/docs/html/guide.html), [Legion](https://legion.stanford.edu/) and other Parallel Global Address Space (PGAS) models, so fleshing out an "advanced" lesson is possible.
    * [OpenOnDemand](https://openondemand.org/) gives a workflow that is accessible to many users
    * Trevor: parallel is about throughput much more than performance, and therefore falls out of scope. Recommend focusing our efforts on MPI with C and Python; applied the "wontfix" label.
    * Taking Benson's point, HPC is broader than PDE solvers, and we should expose learners to a bunch of different paradigms. True, but this issue remains out of scope for hpc-intro.
* [#22](https://github.com/carpentries-incubator/hpc-intro/issues/22), weave a narrative. These can be helpful to maintain engagement and reinforce the concept of why we're doing any of this. Enhancement / final polish, not structural *per se*, but definitely worth doing.

---

## Later Meeting (Americas & Australia)

During this sprint, we will go through the open issues and PRs on [hpc-intro](https://github.com/carpentries-incubator/hpc-intro), triaging and assigning appropriate labels. The goal at the end of the day is to have a set of actionable issues and pull requests, so we can focus our efforts.

### Participants

* Trevor Keller (he/they)
* Wirawan Purwanto (he/him)
* Andrew Reid (he/him)

### Notes

* See inline comments on the Earlier Meeting notes above.
* [#24](https://github.com/carpentries-incubator/hpc-intro/issues/24), maintainer sets. Out of scope for an individual lesson; migrated (by brute copy-paste) to [coordination#32](https://github.com/hpc-carpentry/coordination/issues/32)

* [#154](https://github.com/hpc-carpentry/coordination/issues/154) The fastq files was not found anywhere
    * How to solve: transfer fastqc (bash-lesson.tar.gz) from learner's local machine to the cluster
    * Challenge with fastqc example: not all clusters have it. Many learners do not understand what's fastqc is and what it is for. Or not in ther interest area.
    * How to get around: (1) have a quick install script to make fastqc on a site; or (2) instead of using fastqc, use Nelle Nemo's processing bash script from shell-novice lesson.
    * **TK's recommendation for [#154]**: close this issue; open another issue for removing "fastqc" from the lesson, introduce mpi4py "pi" example and spend more time with it to teach [parallelism and how to run parallel jobs with MPI].

* On the introduction of MPI in the hpc-intro lesson: Is teaching MPI is a must for new learners? Why or why not?
    * Andrew: "something involving MPI is necessary. It's a disservice to our learners *not* to expose them to MPI." Python Pi example is the preferred venue.
        - The jump from serial to MPI jobs is too great.
        - GNU parallel would be a stepping stone: serial to high throughput to MPI
        - flip side: GNU parallel is awkward to use
    * The con of MPI lesson:
        - too much black magic (parts not explained, large jump in concept)
    * MPI and "GNU Parallel" represent two ends of the spectrum of parallel computing: tightly vs loosely coupled problems
    * Reflecting the mission of Carpentries: to teach people an understanding of "what's going on under the hood". The C example of MPI is too much "magic" -- too much blackbox. But because MPI is ubiquituous in HPC everywhere--the "magic" involved in the MPI hands-on does not negate the importance of teaching users about MPI
        - many users use MPI "under the hood" without realizing it
        - Carpentries lessons are not only providing the minimum they need to function, but also to encourage them to grow
    * The reason of using a HPC cluster is to use parallelism. So not to teach parallelism is not right.
    * Mark Piercy: "20% of users use MPI, but they use cluster a lot"
    * The mpi4py "pi" example is a good teaching tool, the computation of "pi" being familiar to virtually everyone

* What important elements of MPI that new users need to be exposed to?
    * job arrays => running in different locations
    * data transport issues arising in MPI

* How long does "hpc-intro" lesson runs for in a real workshop? If we have more time, we can insert more advanced programming paradigms such as shared memory, task-based parallelism, ... 
    * The design length was 4 hr
    * This determines also how deeper topic such as MPI will be covered
    * *Discussion*: What is first order and what is second order? For HPC, teaching the concept of "connecting to a remote machine and do work with that" is first order, whereas leveraging parallelism on that platform will be second order.

---

Looking for old notes? Check our [minutes](https://github.com/hpc-carpentry/coordination/tree/main/minutes)!

General questions or feedback? Contact [team@carpentries.org](mailto:team@carpentries.org).

Inline HTML with `fa` tags refer to [Font Awesome](https://fontawesome.com/icons?d=gallery).

<!--References-->

[conduct]: https://docs.carpentries.org/topic_folders/policies/code-of-conduct.html
[invite]: https://swc-slack-invite.herokuapp.com/
[license]: https://creativecommons.org/licenses/by/4.0/
[slack]: https://swcarpentry.slack.com
