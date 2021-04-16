# April 15, 2021 HPC Carpentry Coordination Meeting

## Time and Venue

This "meeting" comprises two parts, to improve coverage for our global
community: 1200 UTC and 2200 UTC. Volunteers willing to host additional
sessions should reach out on the
[Slack](https://swcarpentry.slack.com#hpc-carpentry) or the [mailing list
](https://carpentries.topicbox.com/groups/discuss-hpc) to notify potential
participants.

- Click to convert [12:00 UTC](
  https://www.timeanddate.com/worldclock/fixedtime.html?msg=HPC+Carpentry+Coordination%2C+1200+UTC&iso=20210415T12&p1=1440)
  to your local time
- Click to convert [22:00 UTC](
  https://www.timeanddate.com/worldclock/fixedtime.html?msg=HPC+Carpentry+Coordination+2200+UTC&iso=20210415T22&p1=%3A)
  to your local time

:::success 
[***Click Here to Join the Meeting!***](https://meet.google.com/gez-aeui-jdx)

The venue is [Google Meet](https://meet.google.com/gez-aeui-jdx).

:::spoiler You can also call in by phone:
Call +1 234-405-0205
PIN: 662 051 554#
To view more phone numbers, click this link: <https://tel.meet/gez-aeui-jdx?hs=5>
:::


**Shared Calendar for HPC Carpentry**

If you have not already, please add the [Google Calendar](
https://calendar.google.com/calendar/?cid=bWp0ZWh0ZmEycmVjZGZtNmZjdGUwMWVhdGNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ)
to your scheduling app so that these are not a surprise. You may also import
the [ical](
https://github.com/hpc-carpentry/coordination/files/6240223/hpc-carpentry.ical.zip)
file directly into your calendar, though this will not receive updates in case
of scheduling upsets.


## Agenda

See the [previous coordination CodiMD](
https://codimd.carpentries.org/5zpJN7jZQ_SChBWz2bvKVg?both). See also
the [accepted process proposal](
https://codimd.carpentries.org/3VbpZ4C5T5eLD9V_0ZJGng).

### State of the Sites

- There are currently multiple issues with the "coordination" tag on the
  [hpc-intro](https://github.com/carpentries-incubator/hpc-intro/issues) repo.
  Some kind of plan of action would be useful.
    - Possibly revive the use of GitHub Projects as a management tool?
- Alan O'Cais and Peter Steinbach taught some of our lessons [last
  month](https://swcarpentry.slack.com/archives/CEXAZR52T/p1616428972013900)
  and offered to collect feedback that might inform our content going forward.
  This is very close to the kind of "road testing" that is very high-value in
  lesson development. Can we capture this feedback? No issues with the new
  "feedback" tag are in the repo.
    
### Governance 

- **Nominations!** Now that we have a reasonably democratic process, we should
  nominate and elect members of a steering committee. See the [coordination
  repo issue](https://github.com/carpentries-incubator/hpc-intro/issues) with
  details of the process. For this meeting, participants can express their
  willingness (or not) to serve, but actual nominations will take place on the
  coordination repo.
- Milestones -- this is an action item from the March 18 meeting. Andrew Reid
  promised to review the [Carpentries Handbook on lesson development](
  https://docs.carpentries.org/topic_folders/governance/lesson-program-policy.html#lesson-program-incubation-roadmap)
  and identify some milestones for a path forward for the lessons.

### Other Business

- Software installation? This is becoming an increasingly important part of
  workflows. Does it fit in our lessons? In a new lesson?

---

### 1200 UTC Session

#### Attending

- Andrew Reid, NIST
- Alan O'Cais, JSC
- Ian Kirker, UCL
- Toby Hodges, The Carpentries (lurking on the notes again due to GoogleMeet connection issues!) 
- Benson Muite
- Trevor Keller, NIST
- Annajiat Alim Rasel, BracU

#### State of the Site

- Coordination issues, no evident progress, what's up? Some of these are a mix
  of "to do" and more like policy questions, maybe a way forward is to split
  out the action items from the policy items.
    - Possible way forward: Do the "to do" parts, close the current issues, and
      open a successor issue with the incomplete policy items.

- Road-test report from the lessons that Alan and Peter taught. Notes are in
  the
  [HackMD](https://github.com/hpc-carpentry/HackMD/blob/main/workshops/2021-03-24-HEIBRiDS_Spring_School.md)
    - Side note: The HackMD can be sync'd via Github, but there's a barrier to
      the sync powers, requires invitation and acceptance. Anonymous users can
      read and write, though.
    - On the HPC Carpentry slack, there's a March 23 discussion of the results,
      with a link to a zip file of survey results in the replies to the
      top-level entry.
    - The lesson went well. There were technical issues with usernames. One
      learner found the level of the material too low, and the pace too slow.
      This was the only really negative feedback.
    - Trevor liked the ice-breaker and jargon-busting portions, high-value in
      promoting learner engagement.
    - Peter taught the new hpc-parallel-novice lesson, which included a Python
      MPI example similar to the HPC-carpentry one. Learners had questions
      about implementation details, which were not practical to explain, had to
      settle for "MPI is legacy, just like that". Survey feedback reflected
      irritation with this.
       - [name=Trevor] will review the recording and pull out an action item to
         address MPI vs mpi4py vs ... (specifying buffer start & length: needs
         explicit initialization, passing empty buffers, etc.)
       - https://github.com/hpc-carpentry/hpc-parallel-novice/issues/13
   - For this lesson, which is for MPI *users*, possibly it's acceptable to
     just explain the characteristics of the tool. Unclear if a deeper more
     developer-focused discussion would be a distraction at this level, maybe
     this belongs in another lesson. (See the pending agenda item about
     building code.)
   - [name=Andrew]: You have to settle for description at some level. Learner
     feedback suggests this lesson was maybe not hitting the right level, but
     such a level exists. Counterpoint [name=Benson]: Some frustration is
     inevitable, we can offer resources for learners to dig deeper on their
     own, but we need to maintain focus on the lesson goals.
   - See issue at https://github.com/hpc-carpentry/hpc-parallel-novice/issues/13

#### Governance 

- We are ready to nominate a steering committee, via an issue in the
  coordination repo. Current quorum is 5, so 5 or more upvotes will get someone
  elected.
    - https://github.com/hpc-carpentry/coordination/issues/44
    - Main idea is to steer contributions towards high priorities of the
      community, and try to focus on progressing towards Carpentries
      acceptance.
        - Strong preference for consensus decision-making.
    - Secondary role is enforcement of the code of conduct, taking action
      against violators.
    - Existing description requires at least 3 active members.
    - Potential nominees should be consulted prior to creating the comment
      nominating them. Not a rule, just a best-practice.
        - [name=Trevor] Because it's on GitHub, public, we don't want to
          embarrass folks. Let's make this a rule.

#### Milestones:


- [name=Andrew]'s action item from prior meetings: review lesson material, to
  get feedback. Progress addressing [name=Mike]'s issues has been slow, murky.
- Goal was to filter action items / to-do items to begin conforming to The
  Carpentries' Handbook.
- The Carpentries outline specific Roles: authors, maintainers, curriculum
  advisors. But all of us are all these things.
    - [name=toby] there will be time later to divide up/formalise
      responsibility. you are making great progress for now so I would not get
      hung up on this yet.
- The Lesson Lifecycle also has neat divisions (pre-alpha (writing), alpha
  (testing), beta (polishing), stable). [name=Peter] donated this curriculum in
  the Alpha stage.
- These models are not sacred, or a requirement: they're intended to guide
  folks who have no idea what to do.
- Harder to apply to our work. The Handbook does not discuss incorporating
  learner feedback at all.
    - [name=toby]: that's something for me to address! If someone would like to
      open an issue on https://github.com/carpentries/curriculum-development/
      ...

:::success
Our highest priority now should be gathering and addressing learner feedback.
:::
* [name=toby]: in light of the above, I encourage you to adjust the life cycle
  stage of hpc-intro to "beta" and put a call out to The Carpentries community
  for volunteers to pilot the lesson further.
    * [name=Andrew] :+1:
    * Issue to advance our Lifecycle ID:
      https://github.com/carpentries-incubator/hpc-intro/issues/338
      ![carpentries-lifecycle](https://user-images.githubusercontent.com/2179347/114876195-166c0800-9dcc-11eb-8789-6bc8d2ae9b15.jpg)
      *Source:
      https://carpentries.github.io/curriculum-development/the-lesson-life-cycle.html#overview-and-definitions*
      - [x] Pre-Alpha
        - [x] Outline the curriculum
        - [x] Publish first draft lesson
        - [x] Organize *alpha pilot workshop* within the author
              community/organization/institution
      - [x] Alpha
        - [x] Host the *alpha workshop* at the authors' host institution
        - [x] Collect feedback from learners & instructors
        - [x] Revise curriculum & lesson(s)
        - [x] Authors teach the lesson
        - [x] Iterate
        - [ ] Organize *beta pilot workshop* for the greater Carpentries community
      - [ ] Beta
        - [ ] Engage with *beta workshops* hosted...
          - [ ] by instructors outside the authors' circle
          - [ ] at institutions outside the authors' own
          - [ ] in countries, regions, and sovereignties beyond the authors' own
        - [ ] Organize "Bug Barbecues" to catch and address lingering issues
            - [name=toby] this is more intended for Official lessons (e.g. Data
              Carpentry Social Science curriculum) and you can safely skip the
              step. But, if you wanted to organise a sprint to fix
              issues/polish the lesson at this stage, [these
              recommendations](https://github.com/tobyhodges/lesson-sprint-recommendations)
              might be helpful.
      - [ ] Stable
        - [ ] Release a polished version suitable for any Instructor to teach 
    
* Maybe the community in Australia that recently chimed in in the slack. They
  have suggested they might attend the 2200 UTC session today.
* We have had prior conversations with [name=Toby] about possibly getting
  resources from the Carpentries for standing up clusters for teaching
  purposes. Re-open that conversation?
    * [name=Toby] I am not on the call and that "?" is ambiguous :laughing:
    * [name=Andrew] Question is for this community, whether to prioritize
      Carpentries resources vs. DIY. [name=toby] thanks for clarifying :+1:
* Clusters that Alan has been providing are based on
  https://github.com/ComputeCanada/magic_castle
  * Anyone interested can sign up to the existing cluster at
    https://mokey.brac.learnhpc.eu/auth/signup


#### Development

Deferred to 2200 UTC for time.

* https://chryswoods.com/main/courses.html
* 

Adjourned!


---


### 2200 UTC Session

#### Attending

* Trevor Keller, NIST
* Andrew Reid, NIST
* Wirawan Purwanto, ODU
* Mike Renfro, TN Tech
* Albert Savary, NeSI
* Annajiat Alim Rasel

#### State of the Site

From Feb 14, 2021 -- 2021 review of lesson text, #297 - #306.

Some of the items raised under hpc-intro coordination are addressed by The
Carpentries [Style Guide](
https://docs.carpentries.org/topic_folders/communications/resources/style-guide.html).

Emphasis:
* No mention of the use of italics or boldface for emphasis
* LaTeX is using italics for emphasis
* Leave this to our judgment call: use **boldface** for emphasis

Proper names:
* Use "Slurm" instead of "SLURM"

#### Brief aside with Albert Savary

* His group has plans to teach the HPC Intro lesson, they have agreed to give
  feedback on issues they encouter. The group is connected with the slack
  conversation of April 13, initiated by Megan Guidry.

#### Governance

Elections! [Click here!](https://github.com/hpc-carpentry/coordination/issues/44)

Purposes of the steering committee:
- foster the HPC Carpentry organization and its lessons,
- guide curriculum development following The Carpentries Handbook, and
  participate in discussions with The Carpentries in a representative capacity
  to help us navigate the pathway to induction as an official Lesson Program.
  An important additional task of this inaugural Steering Committee will be to
  formalize a set of by-laws outlining our governance structure. The time
  commitment of service on the Steering Committee is unknown, but is not
  negligible.


#### Milestones

**Important**: do teach the lessons and gather learners feedback, esp the red
stickies.

How to gather feedback?
- teach the lessons the "Carpentries" way (with pre- and post-surveys).
- issues are second phase of the feedback: from the surveys, the instructors
  would aggregate the responses and report it to the hpc-intro issues
- [name=Annajiat] and [name=Mike] - use "one up and one down" feedback:
  whereeach participation is asked to give one (+) feedback and one (-)
  feedback (optionally: split on the contents and on the presentation)



#### Development

##### Infrastructure for lesson

* The "stable" phase of the lesson still a ways away: setting up environment
  for the lesson is still requiring domain expertise.
* [name=Alan] (in the morning meeting): mentioned MagicCastle VM environment to
  run the lessons.

Are there resources from Carpentries to do the lessons on their VM
infrastructure? 
* Toby's response: it is a tentative "yes". Resources @ Carpentries are
provided by donors.

Alternatives:

* In Europe: LearnHPC - . Is this it?
  https://www.e-cam2020.eu/learnhpc-dynamic-creation-of-hpc-infrastructure-for-educational-purposes/ -
  and is it limited to EU audiences?
  * https://www.learnhpc.eu/
* In US: US academic institutions can leverage XSEDE. Example: IU
  [JetStream](https://jetstream-cloud.org) (VM env with public-facing IP) -
  Mike Renfro is checking with a Jetstream staff member to see if this is a
  fit.
* [name=Annajiat] Alan has kindly provided the VM computing resources for our
  pilot at BracU with supplementary teaching materials from Alan and Wirawan
  Purwanto (thanks)
* AWS - may not be too expensive. Example (WARNING: facts need checking):
  t2.small for 8 hours, cost 4 cents/CPU hour. maybe totaling ~$25 (guessed).
  - Some potential challenges: One difficulty with AWS from our end was even
    the free tier required a credit card which is not owned by all
    [name=Annajiat]
* [CloudBank](https://www.cloudbank.org/training/cloudbank-educators) - also has resources that can be used for education & training
  * Probably not right for our use case: "Any course that utilizes Jupyter
    Notebooks and nbgitpuller links can be set up use the CloudBank Jupyter Hub
    instance."

##### Lesson on "software installation" on HPC

Is this something we should attempt to cover?

* [name=Andrew]: Reluctant to put effort there now.
* [name=Wirawan]: If something is universal enough that it could be reused,
  maybe?
* [name=Trevor]: Software install will open a can of worms. It may be better in
  many cases to ask sys admins to install them for you. For common/universal
  enough software: perhaps there already exists a conda env or Python module
  for that; so not as valuable to add that to our lesson.

Consensus: let's not try covering this for now.
* [name=Trevor] In the configurable section of the lesson, we can add URL to
  local cluster guide re: software install.

There are pluses and minuses on whether users have an understanding how to
install software or not.
* (+) - this gives a better understanding for the users when things go wrong,
  e.g. software users need to have deep enough understanding on the software
  they are using
* (-) - researchers need to focus on research, not on the tools


##### Instructor's Notes

Worth adding on our site to make it easily accessible to potential instructors?

==> Need to modify our hpc-carpentry site to reflect this, resulting in closer
conformance to Carpentries way.

* [name=Annajiat] References: 
https://datacarpentry.org/lessons/
https://librarycarpentry.org/lessons/
https://software-carpentry.org/lessons/
