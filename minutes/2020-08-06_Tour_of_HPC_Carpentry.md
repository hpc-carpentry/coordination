HPC Carpentry - a guided tour
Topic: A guided tour around hpc-carpentry esp. for our new maintainers and members of the new 
HPC-Intro Task Force. Focus areas are
A tour of the lesson material by @psteinb, slides https://codimd.carpentries.org/p/Of5yxC59s#/
An intro to contributing, porting & maintaining the site by @tkphd

This will be an informal conversation, so if you have questions, please ask!

Recording: https://youtu.be/BFTPW8c9eqc
This Etherpad will be archived on GitHub after the session. Please remove any personal information if you don't want it to be archived.
The event will be video recorded. So if you do not want to be on, please mute your video, anonymize your nametag, or take other appropriate actions. You will be notified when recording begins.


date: Aug 6, 2020 at 21h00 UTC
Your time: https://www.timeanddate.com/worldclock/fixedtime.html?iso=20200806T2100

Presenters: 
Trevor Keller, Center for Theoretical and Computational Materials Science, National Institute of Standards and Technology, Maryland, USA. github & twitter: @tkphd
Peter Steinbach, Helmholtz AI Consultants Team Lead for Matter Research, Helmholtz-Zentrum Dresden-Rossendorf, Germany, github:@psteinb, twitter: @psteinb_
HPC-Carpentry: https://hpc-carpentry.github.io/ and https://github.com/hpc-carpentry

Code Of Conduct Facilitator:
Mike Renfro / renfro@tntech.edu
Code of Conduct: 
https://docs.carpentries.org/topic_folders/policies/code-of-conduct.html

Host/Call details
Join Zoom Meeting: ~redacted~

Roll call + Check in:
name / email / pronoun / social media handle 
Trevor Keller / trevor.keller@nist.gov / he, him, his / @tkphd
Andrew Reid / andrew.reid@nist.gov / he, him / @reid-a (gh), @reid_ac (twitter)
Jon Guyer / guyer@nist.gov / he, him, his / @guyer (gh)
Rohit Goswami / rog32@hi.is / he, him / @rg0swami (twitter), @HaoZeke (gh) 
Colin Sauze /cos@aber.ac.uk /he,him / @colinsauze (gh)
Lorna Rivera / lorna.rivera@gatech.edu / she/her/ella / @RiveraResearch (twitter)
Michael Joseph / josephmje.22@gmail.com / he, him / @josephmje (gh)
Dori Sajdak / djm29@buffalo.edu / she, her / @dsajdak (gh)
Peter Lawson / plawson@tulane.edu/ he, him / @pete-lawson (gh)
Evgenij Belikov / e.belikov@epcc.ed.ac.uk / he, him 
Wes Harrell / wes.harrell@vuw.ac.nz / he, him/ @wesharrell (gh)
Mike Renfro / renfro@tntech.edu / he, him / @mikerenfro (twitter, github)
Julia Levites/ jlevites@nvidia.com/ she/ @jlevites
Verónica M.V. / vergaravg@ornl.gov / she,her,ella / @verolero86
Huda Ibeid / huda.ibeid@intel.com / she, her / @hudaibeid
Sajid Ali / sajidsyed2021@u.northwestern.edu / he,him/ @_sajid_a (twitter)

Notes
Collaborative notes
Introductions from Peter, Trevor and Mike
quick poll, who is a carpentry instructor?+1+1+1+1 ++1+1+1+1+ --> About half of us.

Peter's slides: https://codimd.carpentries.org/p/Of5yxC59s#/
HPC Carpentry team founded by ComputeCanada folks
Learner profiles will help, during lesson development, to get the scope aligned with the audience.
20% rule, paraphrased: if the lesson is crafted perfectly, with a large audience, 20% each will be
Bored, you're going too slow
Excited & keeping up
Keeping up & engaged
Falling slightly behind
Frustrated and near giving up every few minutes
The goal (and mindset) is to communicate. Interaction & engagement with learners is important. We need pre- and post-workshop surveys to help calibrate individual instances of teaching the lessons.
Should we archive the hpc-chapel lesson? Introduced by ComputeCanada early on; it is an interesting language, but currently, we have no maintainers for it.
Task Force for HPC Carpentry:
Establish community processes
Develop lightweight & fair governance model
Sharpen lesson content
via weekly coworking hours (up to 90 minutes) to achieve progress on a specific task / unit of work
Limited lifetime: beginning September 2020, close & review in January 2021
Colin: Do we envision having one central version? Or to have each site fork & customize their own material?
Peter: No, and yes. We should move forks ahead in lock-step, but they don't need to be part of the upstream repository.
Rohit: Same with The Carpentries lessons, folks fork & keep a separate instance for each time they teach.
Rohit: Learners should already know bash (files, directories, where you are) before coming to HPC Carpentry.
Peter: Yes; eventually, we will have guidelines for how to construct an HPC "boot camp" progressing through lessons pulled from all The Carpentries, so all skill levels can keep up. Also, this falls under the category of communicating what's expected, before the lesson begins.
Rohit: A lot of this depends on libraries... if you want to learn parallel coding, take some comp. sci. courses. Focus should be on using the tools.
Mike: If our audience is the same as SWC but with bigger problems, I might cull Python & Git and focus in on the HPC-specific material to give it full coverage.
Peter: Yes; those decisions are site-specific. Switching from bio- to physics-centric affiliation, the requirements are vastly different.
Peter: At a lot of sites, people using HPC don't even know about profiling yet.
Rohit: How are we going to structure this? Schedulers, but also lang-specific lessons (Julia, C++). Will these split off?
Peter: I think not. Keep our "farm" as small as possible, focus on low hanging fruit for now.
Might go toward HPC Incubator idea. Might revisit this in the future, if there's big demand for the hpc-parallel session.
Rohit: What about hardware? People don't want to know about it, yet, it's very important. We should have a lesson on this, yeah?
Peter: Be careful about this. Used to open a node and show the guts... might have lost folks there. Read the audience and go off script if necessary.
Julia Levites - NVIDIA has open source GPU intro materials that can be used as a part of the carpentry if interested. this is one example: https://ngc.nvidia.com/catalog/containers/hpc:openacc-training-materials, we are working on CUDA, OpenMP, RAJA, Kokkos and C++ pSTL.
Rohit: Would love to see a link, sounds great ^_^ .
Colin: i'd love to have a carpentries GPU course that I could run. It should probably be semi-separate from HPC carpentry though.
Rohit: So these kind of materials kind of bring up my earlier concern. These have nothing (or little) to do with the HPC you might have at your university. In a sense, these are generally soft-marketing techniques. I've been in multiple OpenACC workshops, and we always have a nice sponsor with P1000 GPUs and all that, but then we go home, and we can't even figure out which CUDA compiles on our heterogenous cluster.
Julia: the link is a container that has all you need to run the lab including the compilers. So it should be safe to run on any cluster.
Rohit: Admins don't allow `docker` to be run by users +1
Rohit: Singularity is a possiblity, but only at a reduced performance setting it is easy to convert to singularity
Rohit: In fact, to bring this around, we want to use our HPC hardware, not waste resources on emulation (even if we somehow have admin access)Are you lookign for installation instructions on how to install or figure out what is already available on a cluster or how to install it? No, the point is those libraries target *hardware* which may not be present on the home cluster, so it isn't all that helpful for people to learn them. Can you use OpenACC to get a speedup on a laptop? (not really). On the nice GPUs at NVidea (yes). On your HPC (not necessarily) --> ergo, not a candidate for HPC carpentries.it works on a CPU as well, can be the first step. Is the criteria for the HPC carpentry - has to work on any machine with any config? No, the criteria is to learn how to work with the hardware at your university. It's like programming in general. The carpentries do not teach "programming" in the classic sense. No data-structures, no algorithmic studies etc, etc. Why? Is it not a step? Yes it is, but the point is that it is not part of the *practical* knowledge required to use, say (for the R lesson) R to make a plot of your results. As another example, consider the `grep` algorithm which is beautiful and the CS view of it is definitely part of most algorithmic design courses. When we teach SWC carpentry, we don't talk about it being a finite state machine etc, we say, look --> `grep`, let us use it. Similarly, the point is not to tell you what you might achieve with Nvidia GPUs. It is simply, look --> 'HPC', lets use it efficiently.
Rohit: Another point is that there are as many tutorials as there are vendors (Tensorflow has a whole bunch). None of them help people learn how to work with the HPC infrastructure, so many don't even know how to communicate with their scheduler, and then they don't use the HPC well, even if they're good on Colab.Understood. 
We recently had Nvidia run an intro to deep learning course for our users. Since then we've had to do a lot of work helping to convert people from using jupyter notebooks and digits to using the same code with proper python scripts and slurm.+++ (have had the same experience)agree, digits is not the tool that should be used...if we were to provide teaching materials for you, what would be the ideal format?
@Colin DIGITS course is being retired and the new one basd on Keras will be introduced in September. So, hope it will help at least a bit.
Trevor offers to tutor anyone who wants help with git and contributing in an environment with multiple forks
There are Git topics of specific HPC interest, like teaching compute nodes to commit and rsync back to a node which can push upstream
Not sure if that'd be a lot of fun though
I'm always concerned that no-one wants to actually learn HPC
Trevor goes over an overview of the Jekyll system along with the Liquid templating language in the context of customizing our present offerings.
Chat discusses  text editors, name-drops all the bests, `ed`, `emacs` and `vim`
In particular, demonstrates relevant shell-fu (sed and friends) to work with the lesson materials efficiently
Also shows the snippet layout for working with different clusters
Ends with the git PR and issue setup
Additional comments on GH actions and Travis

Rohit: Any way to teach this, if you don't have a cluster?
Mike: https://github.com/ubccr/hpc-toolset-tutorial (docker)
Colin: https://github.com/colinsauze/pi_cluster (raspberry pi cluster running slurm, needs at least two raspberry pi's. I sometimes bring along my Pi cluster to my HPC training sessions as it makes the whole thing more tangible than some boxes in a far away rack that nobody ever sees, it also makes a nice backup for when people haven't got their real HPC accounts sorted out.)+

Memory dump of the Zoom Group Chat 

00:12:21        Rohit Goswami:  https://codimd.carpentries.org/p/Of5yxC59s#/1/1 
00:12:56        Lorna Rivera:   Same slides look great on my browser as well 
00:12:59        Andrew Reid:    Slides loaded fine for me also. 
00:14:22        Rohit Goswami:  So would this be subsumed into SWC or would we have a separate instance (I'm thinking in terms of AMY and orgs) 
00:14:44        Trevor Keller:  Separate Carpentry, e.g., Data Carpentries or Library Carpentries. 
00:14:59        Rohit Goswami:  +1 
00:15:02        Trevor Keller:  All under The Carpentries umbrella. 
00:18:50        Rohit Goswami:  I don't think the poll has made it's way to me 
00:18:51        Rohit Goswami:  o.O 
00:19:04        Rohit Goswami:  oh it's in the etherpad 
00:24:30        Rohit Goswami:  Perhaps after the excellent presentation we could discuss the focus (https://github.com/hpc-carpentry/coordination/issues/13#issuecomment-670197158) or is that
 for september? 
00:28:12        Rohit Goswami:  I'm actually reasonably certain that should be before the Introduction lesson 
00:30:38        Rohit Goswami:  I like the Snakemake material, but I do feel like it should be taught in the larger context of being able to control the python environment (pyenv or similar) 
00:30:52        Andrew Reid:    URL for what's on the screen now:https://github.com/hpc-carpentry/hpc-carpentry.github.io/blob/master/our-lessons.md 
00:36:42        Rohit Goswami:  +1 for coworking 
00:44:00        Lorna Rivera:   I have to drop off but if the group is interested in working more with WHPC please let me know - lorna.rivera@gatech.edu or @riveraresearch 
00:52:05        Peter Steinbach:        Hi Lorna, that would be wonderful! 
00:52:33        Peter Steinbach:        We will stay in touch. 
00:53:58        Mike Renfro:    My version of this is on the Carpentry Slack at https://swcarpentry.slack.com/archives/C08BVNU00/p1590413018058200?thread_ts=1590374027.053600 — welcome to use it for whatever is useful. 
00:57:06        Peter Steinbach:        Andy turner adopted the variables templating trick from my material to hpc-intro. 
00:59:10        Andrew Reid:    "Center for Theoretical and Computational Materials Science", for those of you burning to know what CTCMS at NIST is. 
01:03:29        Mike Renfro:    Simple Github workflow: https://guides.github.com/introduction/flow/ 
01:05:07        Jon G.: can we send you hate mail for using emacs? 
01:08:51        Mike Renfro:    We may not. Emacs is a great operating system only lacking a text editor. And Vi is a great editor for configuring the Makefiles I use to build Emacs. 
01:09:33        Rohit Goswami:  Well for SSH systems, it's hard to beat TRAMP+emacs 
01:09:34        Rohit Goswami:  :P 
01:09:52        Rohit Goswami:  it's the lowest overall effort (compared to setting up vim on the HPC AND your machine) 
01:10:11        Andrew Reid:    Ed is the standard text editor. 
01:10:30        Mike Renfro:    By definition. 
01:14:25        Wes Harrell (VUW):      Sorry, have to go, but great to hear about the HPC Carpentry ides and plans. 
01:14:50        Peter Steinbach:        Anytime! Please stay connected, Wes. 
01:16:10        Sajid Ali Syed: Would working groups to improve the contents of each lesson be formed at the meeting in September ? 
01:16:21        Andrew Reid:    I think you double-nested the braces. 
01:17:21        Verónica:       Unfortunately, I also have to run. I am a few mins late to my next meeting. Appreciate the overview of HPC Carpentry! 
01:17:29        Rohit Goswami:  Have we set up jekyll-liveserve? I let that debug for me (it spits out a bunch of errors for these kinda things) 
01:17:32        Peter Steinbach:        you are welcome, please stay connected. 
01:17:38        Verónica:       Will do! 
01:18:32        Peter Steinbach:        Rohit, could you please open an issue on hpc-intro repo with your hint to jekyll-liveserve? I can't oversee at this moment how different it is to our c
urrent setup. 
01:18:46        Rohit Goswami:  +1 will do 
01:20:08        Peter Steinbach:        thanks 
01:20:51        Andrew Reid:    It has "sched.flag.user" 
01:22:47        Evgenij Belikov:        Gotta go, thanks for the update! 
01:23:50        Peter Steinbach:        sure thing, please stay connected. 
01:24:39        Rohit Goswami:  I'm a little vague about the action points post meeting 
01:24:49        Rohit Goswami:  are we waiting for the september meet to decide the user groups? 
01:25:05        Peter Steinbach:        yap, see https://github.com/hpc-carpentry/coordination/issues/17 
01:25:18        Peter Steinbach:        we send out a call for participants then for sure 
01:26:39        Rohit Goswami:  +1 
01:29:05        Andrew Reid:    Lots of reassurances. 
01:29:13        Dori Sajdak:    This was VERY useful.  Thank you so much to all! 
01:31:45        Rohit Goswami:  Why does it take so long? 
01:32:07        Mike Renfro:    The tests? 
01:32:16        Rohit Goswami:  yup 
01:32:48        Mike Renfro:    At least the Travis version was firing up VMs, installing Jekyll, etc, and I don’t think it reused any of that from one test to another. For GitHub Actions, no
t sure. 
01:32:53        Rohit Goswami:  am going through it, it doesn't look like there's very much going on, so I'm quite suprised 
01:32:58        Mike Renfro:    But Jekyll was much slower in practice. 
01:33:05        Rohit Goswami:  Ah ok, yeah I'm looking at the old config, zero caching 
01:33:21        Peter Steinbach:        Alan mentioned that the ruby install steps took most of the runtime. 
01:33:31        Rohit Goswami:  It should take around 5 minutes. The R lessons actually need to compile lessons and take around 8 minutes 
01:33:46        Peter Steinbach:        :man_shrugging: 
01:34:03        Rohit Goswami:  but GH actions seem to be doing alright (I've stayed away from them everywhere as of now ^_^ ) 
01:34:12        Rohit Goswami:  I'm convinced they'll start charging everyone 
01:34:14        Rohit Goswami:  it's a trap 
01:35:46        Dori Sajdak:    Thank you! 
01:36:43        Mike Renfro:    https://github.com/ubccr/hpc-toolset-tutorial 
01:37:25        Sajid Ali Syed: I've used this to learn about slurm plugins : https://github.com/SciDAS/slurm-in-docker 
01:37:41        Mike Renfro:    https://github.com/XSEDE/CRI_XCBC 
01:37:44        Colin Sauze:    https://github.com/colinsauze/pi_cluster 
01:41:10        Andrew Reid:    Thanks for hosting, Peter and Trevor. 
01:41:37        Sajid Ali Syed: Thanks for the overview! 

