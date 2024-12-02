# Second HPC Carpentries Task Force Meeting, October 13, 2020

## Logistics

There will be two sessions, one at 0700 UTC (9am in Central Europe) and one at
2100 UTC (5pm in the US Eastern time zone). The first session will be hosted in
Europe and is meant to be a sane hour for Asia and Australia, and the second
one will be hosted in the US. These times were arrived at in the
[previous meeting](https://codimd.carpentries.org/ct7yfc_LSseoC8mEmbVEiQ?both),
and hopefully work well for most people.

In addition, contributors are invited to make comments and raise additional
points in the
[Github issue](https://github.com/hpc-carpentry/coordination/issues/20) for
this meeting throughout the day. This is something of an experiment in
distributed asynchronous coordination, to help mitigate the fact that a single
meeting (or even two meetings) evidently cannot accommodate all participants.

## VTC Info

### For 0700 UTC, Zoom:

Topic: HPCCarpentry Task Force Coordination Meeting Time: Oct 13, 2020 09:00 AM
Amsterdam, Berlin, Rome, Stockholm, Vienna

Join Zoom Meeting ~redacted~

### For 2100 UTC, Google Meet:

To join the video meeting, click this link: ~redacted~

## Agenda

The agenda is as follows:

- Updates on lesson development
  - Is co-working happening, is it effective?
  - What state are the lessons in?
  - Has anyone road-tested any of the content?
  - Do we want a pedagogical review? Who could do this?
- Interaction with Carpentries
  - How do we decide if we're ready for the incubator?
  - Do we need resources from them? A "stunt cluster"?
  - Style/format issues?
    - Nonsequential lesson numbering
      [has impacts](https://codimd.carpentries.org/tsMOzEaMQYmeesMGpalVRw?both)
    - The
      ["main site"](https://github.com/hpc-carpentry/hpc-carpentry.github.io)
      has an
      [issue](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/22)
      also.
- Governance
  - Model for distributed, asyncrhonous strategic decision-making?
  - External advisory council?
  - Schedule and times for meetings?
- New business

## Notes from the 0700 UTC (Europe/Asia) session

- Participants / Roll Call

  - Peter Steinbach, Helmholtz AI Team Lead @ [HZDR](https://hzdr.de),
    twitter:@psteinb\_ github:@psteinb
  - Toby Hodges, [The Carpentries](https://carpentries.org), twitter: @tbyhdgs
    / github: @tobyhodges
  - Alan O'Cais, Juelich Supercomputing Centre, github:@ocaisa

- Updates on lesson development
  - Is co-working happening, is it effective?
    - we've had one co-working session, hosted (and solely attended) by Alan.
    - Peter: this is natural and coworking needs to ramp up to some degree.
    - Alan: the time is too early for people in the UK/UTC+0/1. Can we move it
      one or two hours later and still keep it convenient for folks in Asia?
    - Peter: Trevor mentioned in the chat that he doesn't feel comfortable with
      the core group deciding on the times and expecting everyone else to make
      it fit for them. Action (Peter): open an Issue in the coordination repo
      and ask people for suggestions. Candidates for hosting should get a bit
      of priority in the voting for a time.
  - What state are the lessons in?
    - The only lessons touched recently are HPC Python and Intro to HPC
    - would love to tackle smaller hpcintro issues in next coworking hours
  - Has anyone road-tested any of the content?
    - Peter: no - one planned soon Nov/Dec time frame
    - Alan: no, but trial run of LAMMPS application-at-scale lesson recently
    - Toby: no
  - Do we want a pedagogical review? Who could do this?
    - Peter: I would like this. In summer I went through intro and python
      lessons and I'm more inclined to focus on this. I've just put up a
      workshop on teaching machine learning and there was some discussion about
      aligning content with learning objectives etc. I think this is an area of
      more immediate concern than "backend" issues.
    - Alan: could take advantage of workshop planned for next month? Use that
      as a starting point to work on this. Loosely based around Carpentries
      instructor training, delivered by Code Refinery, over two half-days.
      Could be a good topic/activity for the learners at that workshop.
    - Peter: I think that's a nice idea if it stays lightweight. But need to
      find a way to make this sustainable - make sure experience from that
      workshop flows back into HPC Carpentry. @Toby: if you have any hints e.g.
      from [Teaching Tech Together](http://teachtogether.tech) and
      [Curriculum Development Handbook](https://cdh.carpentries.org), that
      would be great. Last time I looked, the CDH was rather more technical.
    - Toby:
      - supported bioconductor project (3 new lessons from scratch)
        - interested to learn how to get started with learning objectives
        - would offer to do similar contributions for HPC carpentry community
        - this depends on our will to participate with the Carpentries
          incubator
        - alternative option: query the instructors community
    - Alan:
      - shouldn't we first teach the material and collect feedback?
      - material is fine but ordering is "wrong" and motivation is missing
    - Toby:
      - time is worth investing early on to think about target audience etc
      - time saved down the road having the discussion over and over later
      - better catch structural issues earlier - depends on how concerned you
        are if that will come true
    - Alan: what is the reference to learn how to review material?
    - Toby: for now, the carpentries curriculum development handbook and
      potentially the teachtogether ebook by greg wilson
    - Alan: should we create an issue on this?
    - Peter: I would prefer to provide some specific issues to the wider
      community
      - for example: create a tag for such reviews, then create two issues on
        reviewing the motivation of hpc-intro and the ordering of hpc-intro
      - this way, people have actionable items to focus on
    - Toby: Would like to have a domain expert and one who knows the target
      audience
      - Different perspectives are worth having
      - Looking at:
        - Is audience realistic?
        - Is it going to achieve what it wants to?
        - Are timings realistic?
        - Are exercises well designed?
        - Does it conform to CoC?
      - You should decide whether you want to focus on this "polishing" or
        whether you want to devote time to writing new material.
    - Peter: My feeling is that time is better spent reorganising and polishing
      hpc-intro lesson. Can we create this task for our colleagues on the later
      call to decide? (will bring this up with the US coordination meeting)
- Interaction with Carpentries

  - How do we decide if we're ready for the incubator?
    - entry requirements are very minimal
      - need to include Carpentries CoC
      - needs to be licensed CC-BY or CC0
      - needs to use the lesson template
      - needs to be distinct from other lessons in the incubator
    - from these requirements, putting lessons in is left to our convenience
    - often: people fear that once lesson is into incubator, awareness will
      attract more critical issues -> to Toby's experience: this is not the
      case
    - for Toby: hpc-intro appears ready, the community needs to decide though
    - Alan: open a voting issue to have the community's say
    - Toby:
      - will help to preempt other questions related to this that come up
      - control to continue with the incubator or even take it out remains with
        us
    - You can submit the proposal by opening an issue here:
      https://github.com/carpentries-incubator/proposals/issues
  - Do we need resources from them? A "stunt cluster"?
    - Peter: my impression is that those teaching the material currently do a
      bit of work to prepare material for their local infrastructure. So maybe
      this is something we don't need right now.
    - Alan: working on proposals that might be offered here within the next 6
      months
      - builds on a tool from compute canada (webtool using terraform in the
        backend to build a temporary cluster)
    - Toby: spoke to Erin at Carpentries
      - Carpentries already pays AWS instances for genomics workshop
      - AWS provided credits for this
      - as not many data carpentry workshops are being hold, that these credits
        can be used for other purposes
      - Toby used small teaching cluster on AWS in the past that cost next to
        nothing
      - Toby can provide scripts and docs for this
      - having a consistent cluster environment for teaching can be very
        productive for learners
    - Alan:
      - might have aquired a domain for this precisely -> will check this again
        -> update: Alan owns hpc-carpentry.org
        - [hpc-carpentry.org](http://www.hpc-carpentry.org) is parked. Are you
          sure you don't own [hpccarpentry.org](http://www.hpccarpentry.org)?
      - for having a stunt cluster, having a consistent branding with a domain
        is well worth investing
    - Toby: this is super useful
    - Action (Alan): create issues to track progress domain and creating stunt
      cluster in "the cloud"
  - Style/format issues?

    - Nonsequential lesson numbering
      [has impacts](https://codimd.carpentries.org/tsMOzEaMQYmeesMGpalVRw?both)

      - Toby:

        - using the carpentries lesson template, extend config.yml a field
          `episode_order` which can take an array of filename slugs that fix
          the lesson ordering and takes precedence over filenames, e.g.

          ```yaml
          episode_order:
            - 10-hpc-intro
            - 15-cluster
            - 45-responsibility
            - 20-scheduler
            - 25-modules
            - 30-transferring-files
            - 35-parallel
            - 40-resources
          ```

      - Alan: that would be very welcome!
      - Alan: hpccarpentry switched to remote theme, is that theme uptodate
        with this feature
        - Toby: yes, the remote theme is always most up-to-date

  - The ["main site"](https://github.com/hpc-carpentry/hpc-carpentry.github.io)
    has an
    [issue](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/22)
    also.
    - Alan: opened this issue
      - relates to the fact that contrast and coloring and fonts are hardly to
        read
      - suggested to adopt carpentries.org and reskin it to hpc-carpentry
        "style"
    - Peter: good idea to adopt what has been seen to work
    - Alan: 1 week after issue above was created, the carpentries moved the
      website to AWS or somewhere else
    - Alan: will see to this in a week or so and try carpentries.org out
    - Toby: not too involved in this as there are background tasks performed at
      carpentries.org related to AMY and github API filtered etc.
    - Alan: will do this in a coworking hour

- Governance
  - Model for distributed, asynchronous strategic decision-making?
    - Peter: still working through a lot of material (the turing way,
      teachtogether, martha's rules)
      - once this coordination venue attracts more participants, e.g. martha's
        rules appear worth while for me
    - Toby: contact Kari Jordan on this, she has experience to set up
      governance structure and can provide advice, also can provide guidance on
      what's required for a new Lesson Program to be established
      - governance is a chicken-and-egg problem
      - Toby can help
      - Kari is goto person however also in relation to becoming part of the
        carpentries
  - External advisory council?
  - Schedule and times for meetings?
    - need to give priority to people who can host meetings to choose possible
      time slots, then have people vote on options.
    - coordination meetings: monthly
    - co-working hours: every two weeks
    - Action (Peter): set up an issue for both of these, use those issues to
      establish dates/times, then propagate this info to website, Slack, etc.
    - Alan: if we had the people for co-working we could schedule more slots.
    - Peter: I saw Benson was willing to take over hosting for an additional
      co-working hour.

### Recording

A video recording is available. For access, pelase contact Peter Steinbach or
Alan O'Cais. goo

## Notes from the 2100 UTC (Americas) session

To join the video meeting, click this link:
https://meet.google.com/ist-amyv-vua Otherwise, to join by phone, dial +1
304-790-6281 and enter this PIN: 159 861 909# To view more phone numbers, click
this link: https://tel.meet/ist-amyv-vua?hs=5

- Participants

  - Andrew Reid, NIST, github:@reid-a, he/him
  - Trevor Keller, NIST, @tkphd, he/him
  - Evgenij Belikov, EPCC, he/him
  - Jon Guyer, NIST, gh:@guyer, he/him

- Updates on lesson development
  - Is co-working happening, is it effective?
    - Had a successful evening co-working session. Wrote a PR, just merged!
    - Current meeting times are 8AM or 11PM in the UK, which is not ideal. More
      convenient sessions require available hosts.
  - What state are the lessons in?
    - HPC-intro is in good shape, lots of content and attention.
    - Other lessons are mostly dormant.
  - Has anyone road-tested any of the content?
    - Possible near-future opportunity at NIST.
    - Otherwise, no. Feedback on re-sequencing to improve flow would be
      welcome.
  - Do we want a pedagogical review? Who could do this?
    - Yes!
    - Trainers Community? HPC neophytes, but experienced educators.
    - Chandler Becker @ NIST has offered to look over or provide guidance on
      curriculum development.
- Interaction with Carpentries
  - How do we decide if we're ready for the incubator?
    - Trevor thinks hpc-intro is ready.
      - Getting it in the Incubator reduces our risk of getting scooped by
        another organization. (Like CodeRefinery? Not much risk here.)
      - Making it an agenda item for Thursday's co-working hours
    - hpc-python, maybe not so much?
  - Do we need resources from The Carpentries? A "stunt cluster"?
    - It would certainly help. It's a want, not a need.
    - ComputeCanada might be able to provide this
      - Tool to spin up a cluster, not money or cluster credits.
    - Alan own an hpc-carpentry themed domain, which might simplify writing up
      the resource
  - Style/format issues?
    - Vocab: Templates _vs_ Themes _vs_ Styles _vs_ ~~Rubriks~~ Rubrics
      (Rubriks are cubes) _vs_ Motifs
      - Need to double-check whether our lessons' styles are up-to-date with
        [The Carpentries](https://github.com/carpentries/styles).
      - Motif?
    - Nonsequential lesson numbering
      [has impacts](https://codimd.carpentries.org/tsMOzEaMQYmeesMGpalVRw?both)
      - Action item for Thursday coworking hour.
    - The
      ["main site"](https://github.com/hpc-carpentry/hpc-carpentry.github.io)
      has an
      [issue](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/22)
      also.
- Governance

  - Model for distributed, asynchronous strategic decision-making?

    - Model question is separate from decision models like Martha's Rules,
      Turing Way.
    - Volunteer-driven, vaguely anarchistic...

      > the way British parliament used to work, where the Lord who proposes an
      > idea funds & implements it

      A bit anarchistic.

    - Direct democracy
    - _Meritocracy_ == _Chronocracy_: if you put in the time, you get the
      influence. Trying to steer away from this to build an inclusive, diverse
      community.
    - Conflict resolution protocol
      - Marks on the floor 2 sword lengths apart ("toe the line")

  - External advisory council?
    - Do we want one? Who would they be? Do we have friends in high places?
    - HPC Professionals who aren't involved for technical advice; reciprocity:
      here's what it would take for our HPC center to teach or recommend your
      lessons
    - Carpentries members & non-HPC professors for pedagogy
    - Do we know anybody?
      - XSEDE, TACC, NERSC -- helps develop resources / materials for everyone
        involved
      - Colleagues, spouses? Random folk on the street? What's in it for them?
    - Posters at Nvidia GTC, Supercomputing, ...
  - Schedule and times for meetings?
    - Contribute to issues on the Coordination repo as they come up
    - Attendees from the first coord meeting are attending... which excludes
      much of our community

- New business
  - Nope.

---

General questions or feedback? Contact
[team@carpentries.org](mailto:team@carpentries.org).
