# HPC Carpentry Community Call

December 20, 2018; 5pm GMT / 12pm EST / 9am PST

Planning issue: https://github.com/hpc-carpentry/coordination/issues/1

Notes: https://pad.carpentries.org/2018-12-20-hpc-carpentry

## Abbreviated Notes From Etherpad: 

### Attendees
* Trevor Keller, NIST, have taught intro to GPU
* Alex Razoumov, Westgrid (compute canada), hpc-chapel (10 times a year)
* Andrew Reid, NIST, administrator, transition to shared resource andrew.reid@nist.ogv
* Martin Callaghan, leeds, lots of training + teaching, have done the HPC Carpentry
* Bob Freeman, Harvard Bizness, HPC stuff on + off for past four years, doing more w/ hands-on
* Dima Shyslov, Univ of Ariz, intro tutorials for classes
* Richard Barnes, phd student at UC Berkeley, adapt code to HPC (or GPUs)
* Elsa, LLNL, work in computing center, training, 
* Dirk Collbry, Mich State, teaching a class in the spring
* Pariksheet, grad student at UConn, got into carpentries + HPC at same time, increase training for users
* Tim Haines, former PhD grad @ UW Madison, DoE's exascale computing program; thaines.astro@gmail.com
* Jean Shuler, LLNL, has summer intern programming 
* Xiaohu Guo, , CFD, training
* Marina Kraeva, Iowa State University
* Trevor Keller / NIST (MD US) / trevor.keller@nist.gov
* Marina Kraeva / ISU / kraeva@iastate.edu
* Pariksheet Nanda / University of Connecticut / pariksheet.nanda@uconn.edu
* Rintu Kutum / CSIR-IGIB, New Delhi, India / rintu.kutum@igib.in 

### Agenda
* Summaries of recent HPC Carpentry workshops
* update on current status of lessons, priorities
* questions from attendees (either live or from comments below)
* pathways for people to get involved
* planning for future calls

   
### Notes

**Summary of run workshops:**

* Martin: Univ of Leeds, 25 people attending, in general many of the same comments as those listed on
materials may need to be done with pick as you need when running the workshop
* Andy: see Github issue

* Martin:
    * Broad spread of what people what.  Materials might be part of a pick and mix collection.  Selection and tailoring.
    * Iterating through the carpentries like other lessons we get to learn from everyone else's experience.
* Christina:
    * We need to have a lot of this customization!
    * How do we make it easier to make your own putting together component pieces together?
* Martin:
    * Having a model workshop you can deviate from is very useful
* Peter:
    * Many people mix up putting nitty-gritty details of their cluster in the materials.
    * We need core concepts and then dive into site-specific stuff.
    * Put into notes so that contributors are aware of this.
* Christina:
    * Also notes for people teaching the lesson.
* Tim:
    * Has anyone tried GitHub content management system before:
    * http://paislee.io/how-to-use-github-as-a-minimal-cms/
* Christina:
    * We currently add in our own layer of templating.
* Peter:
    * What's the goal?
    * We have an HPC landing website with instructions for extending it.
    * Are we going in that direction or is that dropped?
* Christina:
    * Where would you go to run a workshop?  How to customize?
    * Should we have a blog?  Should it be stored in a repository somewhere?
    * hpc-carpentry.github.io 
    * github.com/hpc-carpentry/coordination 
* Elsa:
    * Have a master list of some repositories.  A master HPC lesson that each organization can fork and have their own information and branding for their clusters.  Link back with here's a list of people who have their own lessons that are modified you can look at.
* Andrew:
    * Show an example of a basic unmodified lesson and a customized lesson and make it easy to see the diff between the 2.
    * When I got into HPC carpentry, finding the official site was hard.  Finally found it from looking for Christina's name from SciPy.
    * Hard to find the real HPC carpentry.
    * Needs fixing.
* Christina:
    * Put in the notes when you google what shows up.
* Pariksheet:
    * I get the correct first link https://hpc-carpentry.github.io/ when searching for "HPC carpentry" with Duck Duck go
* Christina:
    * (Responding to Richard) Customization could occur at a lot of levels.
    * As much as possible should be site specific.
    * Content changes should be fed back to the template.
    * HPC Carpentry is not a formal organization so it's hard to say how people get involved.
    * Like the carpentry lessons there are markdown files which get edited to make the website.
    * We need maintainers!  If that sounds interesting to you, please follow up.
    * Let's take a quick glance at the lessons to see where people are interested in getting involved and what they would like to do.
    * Things we would like to see or prioritize.  "If we have this, that would be great!"

* Peter: HPC-Intro is in a transition state right now. A story has been started, but stops abruptly after Lesson 2/3. 
   * In need of review and feedback! Personal investment in moving it forward, hopes to get more investment to get it stable & polished over the next few months (Q1-2019).
   * We need a reasonable, stable version of HPC-Into for people to fly around on the cluster.
   https://hpc-carpentry.github.io/hpc-intro/
* Christina:
   * HPC-Intro and shell are the most active at being reshaped and tweaked,
* Bob:
    * Thanks Peter for adding that!  I spoke with our research computing group about using the materials.  We plan to use in February or May of this year.
    * Talked with Christina and a few others with the cognitive jump from not doing batch work to batch jobs.
    * Having a road map would be helpful to see where the end point of the lesson are.  What are the objective and commands being taught?
    * For example, I'm not sure I want to teach how to teach people hwo to ssh into a compute node and teach them to use the kill command; on a roadmap we would discuss whether that is really an appropriate thing to teach.
    * We should talk about what is etiquette on an HPC system.  Would mean slowing things down a little bit, but for a core group of people would allow the community to make major changes to some of the lessons.
    * Thanks for explaining the Intro and shell lessons are still in transition.
* Tim:
    * I'm curious about the scope of HPC carpentry.  Currently there's how to login to a node, sbatch commands, PBS.  Chapel on the other hand is very specific beyond the core fundamentals of using an HPC system.
* Alex:
    * The original goal behind HPC carpentry was having it modular so everyone can contribute.  We went to Chapel for many reasons; it's high level and supports distributed and shared memory.  Much more high level.  If you need an MPI module, feel free to develop it.  We pick up what we want.  The original goal was to have a choice between HPC python and HPC chapel.  There are other things people do that are unpublished.
* Christina:
    * The curriculum is meant to be modular.  Like an HDF5 lesson.  Adding in lessons is a lot of work!
    * We teach at least HPC-intro and HPC-shell.  The target audience might not need any of that extra stuff.
    * People who can no longer run on their own computer and have to use the cluster is our learner profile.
    * They would leave having practiced submitting a job and have an idea of the terms to solve a problem or understand the admin e-mails.
* Peter:
    * I see the point that there needs to be a roadmap.  A steering committee might be a good idea.
    * Focusing on HPC-intro.
    * There is a high interest from different groups, but interest has a curve downwards.  People don't have time.  Discussions on GitHub take a long time, but they are very fruitful.
    * Outline: https://github.com/hpc-carpentry/hpc-intro/blob/gh-pages/lesson-outline.md
* Bob:
    * Steering committee not a bad idea of a core group deciding together what directions to take the lessons in.
    * This way we don't see the lessons going down one very specific path of a particular discipline or way that technologists use the cluster.  Should be broadly usable by as many sites as possible.
* Christina:
    * We have a lesson outline!  If people have strong feels or opinions about the direction of the lessons and discuss amongst themselves.  Most of the maintainers know what we are trying to accomplish and are going to focus on that material.  Having community feedback is important.  The easiest way to do that would be to follow the repositories you care about and we can use these calls to follow up on things that need major discussion.
* Bob:
    * Making sure things map from the outline to the lesson modules and have regular check-ins on it.
    * I'm afraid of using mailing lists and GitHub repos can be asynchronous of people wanting to make decisions and waiting for replies.
* Christina:
    * We need to eliminate confusing entry points from HPC and say where to get started.
    * HPC-intro maintainers and interested folks should plan a meeting in the new year.
    * For new maintainers someone will be in touch about adding you to the GitHub organization.
* Peter:
    * If there's anything you want to share, use the mailing list, open issues!
* Christina:
    * Sometimes replies are slow but everyone is doing the best they can!  Keep inching forward.
    Will issue a call for January.
