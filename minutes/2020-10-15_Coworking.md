# HPC Carpentries Coworking Hours

The HPC Carpentries Task Force holds coworking hours every other Thursday, with three time slots intended to provide adequate coverage for our global constituency. Times are subject to change, after discussion & voting via GitHub [Issues](https://github.com/hpc-carpentry/coordination/issues), so please speak up (or open a new issue) if you are unable to attend due to permanent conflicts with the existing time slots.

Check your local times below, and join whichever is most convenient. If you have a permanent conflict and can attend none, please contribute to the [open discussion](https://github.com/hpc-carpentry/coordination/issues/21) on revising the European time, open a new issue for other meetings, or both. 

The meetings will be held, with audio & optional video, through the `#hpc-carpentry` channel on The Carpentries' Slack. To join, click [this link](https://swc-slack-invite.herokuapp.com/). If you have already joined, login through [this link](https://swcarpentry.slack.com). 

Thanks, and see you soon!

### Check your local times

* Europe: [7:00 AM UTC](https://www.timeanddate.com/worldclock/fixedtime.html?iso=20201015T0700&msg=HPC+Carpentries+Coworking+Hour+Europe)
* Asia: [1:00 PM UTC](https://www.timeanddate.com/worldclock/fixedtime.html?iso=20201015T1300&msg=HPC+Carpentries+Coworking+Hour+Asia)
* America: [9:00 PM UTC](https://www.timeanddate.com/worldclock/fixedtime.html?iso=20201015T2100&msg=HPC+Carpentries+Coworking+Hour+America)

---

## Europe+

The current timeslot for Europe+ is 7:00 AM UTC, though this is being [actively discussed](https://github.com/hpc-carpentry/coordination/issues/21). 

* Hosts: ~~Peter Steinbach &~~ Alan O'Cais
* Check your local time [here](https://www.timeanddate.com/worldclock/fixedtime.html?iso=20201015T0700&msg=HPC+Carpentries+Coworking+Hour+Europe).

### Participants

* *name*, *pronouns*, *interests*
* Alan O'Cais, he,him,  (struggling to know what is meant here)
* Benson Muite, he/him , HPC; PGAS

### Agenda

* Adopting Carpentries landing page style
  * See [the proposal](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/26) and [the accessibility issue](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/22) that partially motivated it
  * I'll prepare a PR that makes the move and will point hpc-carpentry.org (which I bought a while ago so we wouldn't get scooped) to my branch for the time being.
    * This was discussed a bit about how to do this and how to make it welcoming for new material from other sources
    * The incubator page exists on the Carpentries page and would be part of our clone, one option is to use that

## Asia-Pacific

* Hosts: Annajiat Rasel & Benson Muite
* Check your local time [here](https://www.timeanddate.com/worldclock/fixedtime.html?iso=20201015T1300&msg=HPC+Carpentries+Coworking+Hour+Asia).
* https://meet.jit.si/LengthyPredecessorsSkipAfterwards
* 
### Participants

* *name*, *pronouns*, *interests*
* Benson Muite, he/him, HPC; PGAS
* Annajiat Alim Rasel, he/him, HPC/HPS, NLP/ML, Distributed Systems

### Agenda

* [Chapel](https://hpc-carpentry.github.io/hpc-chapel/)
* [PCJ](https://pcj.icm.edu.pl/)
* [XcalableMP](https://xcalablemp.org)


#### Notes

### Material links
https://github.com/FZJ-JSC/tuning_lammps
https://schema.org/
https://github.com/ComputeCanada/magic_castle
https://pbdr.org/
https://schema.org/docs/gs.html
https://github.com/hpc-carpentry/coordination
https://github.com/hpc-carpentry/hpc-chapel/blob/gh-pages/lesson-outline.md

### Suggestions
Workshop before December, prefer to start in late October

Application areas of interest:
NLP, Machine learning, Visualization, GPU programming, CUDA, OpenGL

Timing: Fridays 12 UTC - 15 UTC

Participant background: Mostly Java, then Python, and C/C++

Pre-workshop survey design 

Resources:
A guide for shell scripting
https://tldp.org/LDP/abs/html/
https://tldp.org/guides.html

#### Parallel Java
https://pcj.icm.edu.pl/

#### DeapSecure
https://dl.acm.org/doi/10.1145/3332186.3332247
http://www.ccpo.odu.edu/~klinck/Reprints/PDF/purwantoDeapSecure2020.pdf
https://github.com/x10-lang
Associated course 
https://online.rice.edu/courses/parallel-programming-java/
Paper on teaching parallel Java
https://www.researchgate.net/profile/Bryan_Carpenter/publication/266396774_Teaching_Parallel_Programming_Using_Java/links/54b7be8e0cf24eb34f6ed739.pdf?disableCoverPage=true
Java bindings for OpenMPI 
https://www-lb.open-mpi.org/faq/?category=java
https://github.com/mboysan/ping-pong-mpi-tcp

#### Parallel Sage math materials
https://doc.sagemath.org/html/en/thematic_tutorials/numerical_sage/mpi4py.html
Seems one can mostly use Python in parallel
https://sagecell.sagemath.org/
pretextbook.org

#### Debuggers and profilers
https://github.com/jupyter-xeus/xeus-python
https://github.com/jupyterlab/debugger
www.cs.uoregon.edu/research/tau/home.php
https://www.arm.com/products/development-tools/server-and-hpc/forge
https://totalview.io/products/totalview
http://pramodkumbhar.com/2018/06/summary-of-debugging-tools/
https://researcher.watson.ibm.com/researcher/view_group.php?id=536
 

## Americas

* Hosts: Trevor Keller & Andrew Reid
* Check your local time [here](https://www.timeanddate.com/worldclock/fixedtime.html?iso=20201015T2100&msg=HPC+Carpentries+Coworking+Hour+Europe).

### Participants

* *name*; *pronouns*; *interests*
* Trevor Keller (NIST); he/him; GPU, I/O, microstructure
* Mike Renfro; ; 
* Andrew Reid (NIST); ;

### Agenda

* Requirements to join the Incubator


### Notes

Mike has started work on a Bandwidth & Latency diagram. Looks good so far!

Poked around with manual lesson ordering. It works!
The trick is to enumerate the lesson file names, *without* the `.md` extensions, in your site's `_config_options.yml`. We can start renaming.

```yaml
episode_order:
    - 11-hpc-intro
    - 12-cluster
    - 18-responsibility
    - 13-scheduler
    - 14-modules
    - 15-transferring-files
    - 16-parallel
    - 17-resources
```

#### Incubator requirements

https://github.com/carpentries-incubator/proposals


[What are the requirements for being included in The Carpentries Incubator?](https://github.com/carpentries-incubator/proposals#what-are-the-requirements-for-being-included-in-the-carpentries-incubator)

- [x] Your lesson/proposed topic should be distinct from existing official and community developed lessons. 
  - HPC-intro in particular is distinct from other content in the incubator. The less-developed lessons are as well, with the possible exception of HPC Python, which may overlap with some Snake-make efforts. Modifying this lesson to get to HPC-Python and incorporate existing material by reference should be straightforward.
- [x] Your lesson must use our lesson template and conform to our Code of Conduct.
  - We are confident that we are using the Carpentries template. We refer to their remote theme at build-time, and also the "episode_order" thing totally worked, and it relies on functionality inherited from the Carpentries infrastructure.
- [x] Your lesson is licensed CC-BY or CC-0.
  - We are using CC-BY 4 as our license.  It's in `LICENSE.md` at the top of the hpc-intro repo, and is in fact copied from the Carpentries.
- [x] The displayed life-cycle stage of your lesson fits with the recommendations in [Chapter 7 of the Curriculum Development Handbook](https://cdh.carpentries.org/the-lesson-life-cycle.html#overview-and-definitions).
  - For the curriculum-development material, we've been working within the Carpentries model for some time, but should double-check that we're on solid ground here. HPC-intro is in [*alpha* state](https://github.com/hpc-carpentry/hpc-intro/blob/8102c9e998acf4ba778d7c16d13631b40af4639a/_config.yml#L80).
- [ ] Your lesson follows The Carpentries approach to curriculum development detailed in our [Curriculum Development Handbook](https://cdh.carpentries.org/the-lesson-life-cycle.html).
  - Peter Steinbach has mentioned the Handbook several times, so we can assume that the bulk of HPC-intro conforms. Or, we can double-check.

---

General questions or feedback? Contact [team@carpentries.org](mailto:team@carpentries.org).
