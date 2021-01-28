# January 2021 HPC Carpentry Coordination Meeting

## Date and Time:

Proposed for Jan. 21, 2021, time TBA -- prior meetings have had success with sessions at 1200 UTC and 2200 UTC, with additional sessions if someone is willing to host.

- Time conversion for [12:00 UTC](https://www.timeanddate.com/worldclock/fixedtime.html?msg=HPC+Carpentry+Coordination%2C+1200+UTC&iso=20210121T12&p1=1440)
- Time conversion for [22:00 UTC](https://www.timeanddate.com/worldclock/fixedtime.html?msg=HPC+Carpentry+Coordination+2200+UTC&iso=20210121T22&p1=%3A)


## Venue

Both meetings used [Google Meet](https://meet.google.com/gez-aeui-jdx), updated Jan. 21 with a new URL. 

## Agenda

### State of the Sites

- HPC-Intro is now in the incubator! Thanks to Trevor Keller for getting it done, and Toby Hodges for assisting with the migration.
    - Folks who want write access should join the [hpc-intro-maintainers](https://github.com/orgs/carpentries-incubator/teams/hpc-intro-maintainers) group in the [carpentries-incubator](https://github.com/carpentries-incubator) organization on GitHub.
      How?
        - Ping [Trevor <i class="fa fa-envelope-square fa-fw"></i>](trevor.keller@nist.gov) or [Toby <i class="fa fa-envelope-square fa-fw"></i>](tobyhodges@carpentries.org) to request an invitation to the Team.
        - List your <i class="fa fa-github fa-fw"></i> GitHub handle here! Trevor will add you.
          - [ ] *e.g.,* Trevor Keller: tkphd
          - [ ] `wirawan0`
        
    - There are still many legacy issues. What criteria should we use to group and prioritize these?
     

- [HPC-carpentry.org](http://www.hpc-carpentry.org) is live, and has some new content. Is content migration complete?
  - We have a new logo! It's [issue #28](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/28) on the non-migrated hpc-carpentry.org site, and the winning entry is [Entry 5](https://github.com/hpc-carpentry/hpc-carpentry.github.io/issues/28#issuecomment-729230704) from Mumtahinah Sristy.
    ![mumtahinah_sristy](https://user-images.githubusercontent.com/2179347/99453905-a0827400-28f3-11eb-8d61-49702defae76.png)
  - We can start to incorporate this into our sites.

- An introduction to parallelisation. (Peter won't be able to join the coordination meeting, but would appreciate if people could discuss.) Feel free to leave thoughts in the discussion notes in this notebook or [here](https://github.com/hpc-carpentry/coordination/issues/29).
  - I propose to include [psteinb/hpc-parallel-novice](https://psteinb.github.io/hpc-parallel-novice/) into hpc-carpentry. Proposal: <https://github.com/hpc-carpentry/coordination/issues/29>
  - the material was taken from [hpc-in-a-day](https://github.com/psteinb/hpc-in-a-day) and is ready for being taught
  - the lesson itself takes learners through the basic steps from serial to parallel code using python
  - I taught this lesson about 10-12 times by now (2 times in 2020) to different audiences
  - the lesson starts with profiling serial code, calculating an expectation what to gain from parallelisation and the diving in to several parallelisation schemes:
    - shared memory parallelisation with `multiprocessing`
    - distributed parallelisation on a client-server architecture with `dask`
    - high-throughput parallelisation using one-job-one-file approaches and map-reduce
    - bonus: a guided tour through distributed parallelisation with `mpi4py`
    - a gpu lesson is missing for now
  - I believe, hpc-carpentry currently misses a introduction to parallel computing compatible with the average novice HPC user, so I think this would be a nice addition.

### Governance and Interactions with Carpentries

We face a challenge with trying to balance a low barrier to entry and ease of getting things done against some formal structure and an ability to prioritize and direct effort within the HPC carpentry project. So far, an informal self-selected team has mostly driven the process, with feedback from folks willing to speak up.

The Carpentries has resources to help with governance, and we have identified some of our own. The "big question" of this agenda item is, what is our collective impression of the available resources, and how can we move forward? Should we have a formal leadership structure?
  - Trevor: note that, from the [Carpentries Handbook](https://docs.carpentries.org/topic_folders/governance/lesson-program-policy.html#lesson-program-incubation-roadmap), we are required to have *some* leadership structure:
    :::success
    Establish a culturally and linguistically diverse Lesson Program Committee (LPC) of at least three people to serve as a governance body and point of contact with The Carpentries. The LPC should meet at least quarterly to oversee Lesson Project activities.
    :::

Prior meetings' action items were to read and form an initial impression of (at least) the first two resources below, and then reach out to experts, particularly Kari Jordan, for advice.

#### Questions

* How would we characterize our present governance model?
* Who makes ultimate decisions for the project?
* Who gets to have a say in decisions?
* Are we doing enough to solicit input? (People who miss these vidcons are not well represented.)
* Are we adequately capturing and delivering on action items?
* Would Martha's Rules provide an appropriate, acceptable framework for discussion & decision-making?
  - Please [comment and vote](https://github.com/hpc-carpentry/coordination/issues/28)!

#### Resources:

   - The Carpentries Handbook chapter on [governance](https://docs.carpentries.org/topic_folders/governance/)
       - Specifically the section on [Lesson program Incubation](https://docs.carpentries.org/topic_folders/governance/lesson-program-policy.html#lesson-program-incubation-roadmap)
   - [Martha's Rules](https://third-bit.com/files/2020/08/marthas/) of order, as described by Greg Wilson, proposes a useful mechanism for asynchronous consensus building using GitHub issues. This seems more formal than our efforts have been to date, but may serve our needs going forward.
   - [Opensource.org](https://opensource.guide/leadership-and-governance/) leadership document
   - [TeachTogether](http://teachtogether.tech/en/index.html#s:community-governance) community-governance guide
   - [The Turing Way](https://the-turing-way.netlify.app/collaboration/new-community/new-community-guide.html) guide for new communities.
   - [A Short Guide to Consensus Building](http://web.mit.edu/publicdisputes/practice/cbh_ch1.html): can everyone live with the final proposal; that is, after every effort has been made to meet any outstanding interests?

---

### Session 1 notes

Attendees: 
1. Lex Nederbragt
2. Toby Hodges
3. Andrew Reid
4. Alan O'Cais

#### State of the site:
State of the site is pretty good, the transition to the incubator is complete, lots of contributors have been added, and the process is clear and well-documented.

There are lots of issues and 4 PRs that can't be merged. 

* What to do to merge these? 
  - Trevor:
      - PRs must pass review before they can be merged. Please view the files changed, check that the PR passed all tests, and Add Your Review.
      - If a PR cannot be merged automatically, we have to fast-forward the base of the PR to branch off the current tip of `gh-pages`, a process called [rebasing](https://dev.to/matks/what-it-means-to-rebase-a-pull-request-submitted-on-github-5717).
      - The process produces one new commit for each PR commit. Once the rebased PR branch is updated on GitHub, the code must be reviewed again.
      - We have had better, but not great, engagement with the review process. More reviewers, please!
  - Toby: 
      - Have some sprints (like our co-working hours, but 3-4 hours long), and have the group engage with the issues and make decisions about clearing them. Maybe assign these to the co-working day -- 1st co-working session can do triage, 2nd session can review and maybe re-classify, so the end product is an actionable list of items.
     * Sprint session on other lesson work for developing the lesson. Someone on the sprint will go through the issues, and can raise them with others.
    * On next co-working, EU call can group issues into close-able and unsure, and that can be vetted in the other session, then you can close any left on the "to-close" list after that. Leave a message explaining why it's being closed, and invite the poster to reopen if they think the issue is still "live."

#### Logo

The full set of graphical assets is on Google Drive [here](https://drive.google.com/drive/u/0/folders/1oaOQlAQhErZSwpcqKidrCldlJdZXTZAf). There are some issues, the banner is not obviously extensible to the left and right, and the images are not SVG's. Alan will get in touch with Mumtahinah Sristy to get the practical issues addressed.

#### Intro to Parallelization

The figure in [parallel-estimate](https://psteinb.github.io/hpc-parallel-novice/02-02-parallel-estimate/) gives a good impression of the advantages of parallelisation. 
Not completely obvious if this would replace the C example or live next to it. C example includes some "magic" where we blow past the compiler and the code (because it is out-of-scope for the lesson). Advantage of this Python lesson is that we don't have that. A lot of HPC resource users should learn at some point how MPI stuff works, so this should be part of what we teach. 
The material is very good. We agree it is a good idea to include the lesson in HPC Carpentry.
It will need some updating e.g. for more queuing systems, but these are not difficult to fix.

#### GPU material

Toby is expecting to see at least one lesson on this appear in the Incubator soon. There is already the GPU Speedups lesson.
GPU is conceptually difficult to teach. A lot of things to think about. Need to carefully choose scope and be very clear about your objectives. What do you teach? OpenMP? Something proprietary like CUDA, OpenACC? This choice will also impact who the target audience of the lesson is and vice versa.
There is presently a [GPU speedups](https://github.com/carpentries-incubator/gpu-speedups) lesson in the incubator for the GPU piece, and significant interest in addressing this issue.

#### Carpentries Programs

Library Carpentry is the most recent new Lesson Program (and the only one since the merger that created the current organisation, The Carpentries). HPC Carpentry could be a good candidate for another program. New lesson template coming later this year, and efforts being made to allow for a smooth process for existing material to adopt the new template.

#### Governance

Martha's Rules include requirement for a quorum to make decisions. 50% requirement would be challenging if this includes the full community. If it only includes governing body, this would be more plausible. (Note: Carpentries Executive Council is considering using Martha's Rules for decision-making.) There is a requirement for some established governance structures for a new Lesson Program to join The Carpentries.

Identifying the community: Ask people to self-identify from e.g. the contributors to the repo, members of the slack channel, or recipients of the [topicbox/discuss-hpc](https://carpentries.topicbox.com/groups/discuss-hpc) mailing list -- set a deadline, people who self-identify become community members and can vote on the steering committee memberships down the road.

Self-identification could be clicking the :+1: emoji reaction to the GitHub issue, or posting a response under the issue. (posting a response might make it easier to note down everyone's usernames etc (hovering over an emoji to see who has clicked it is not very helpful...))

For executing on some issues, we could solicit external funding, which could be used for a paid developer to help with lesson issues. Also demonstrates a level of seriousness and engagement to the Carpentries.

Raise these questions to Kari Jordan when we reach out.

---

### Session 2 notes

Attendees:

1. Trevor Keller
2. Andrew Reid

* Peter can transfer ownership of hpc-parallel at will; we would be happy to have it.
* Much ado about quora.
* Plan for a long, combined Sprint next Thursday to evaluate & triage our 51 issues?
    - Opening offer: first meeting flags issues, second meeting reviews & executes
    - Alternative: One combined meeting, discuss each issue as a whole one-by-one and keep or close with extreme prejudice.
        - Those who can't make the joint Sprint (Pacific US, NZ, moonbase alpha) can weigh in & re-open asynchronously?
        - Difficult global coordination poses an obstacle to a joint sprint.
    
* Should we have elections?
  - Reach out via our 3 comms channels to learn who's in the community
  - Request nominations & endorsements for a steering group
  - Leadership happens?

#### Action Items

- [ ] Alan: reach out to Mumtahinah Sristy for a more complete graphics suite based on their winning design
- [ ] Trevor: Schedule a Sprint (or two) to clear Issues and PRs
- [ ] Trevor: Revise Martha's Rules proposal to clarify intent (just the GitHub Issue for discussion & thumbs-up, thumbs-down mechanism for weighing in)
- [ ] Peter: "Indeed, one of my TODOs this year will be to investigate with Kari and others from the carpentries team, how our community can move closer to the carpentries. For this, the roadmap @tobyhodges shared is the recipe to go along with." ([Slack, Jan. 12, 2021](https://swcarpentry.slack.com/archives/CEXAZR52T/p1610546969088300?thread_ts=1610477011.086500&cid=CEXAZR52T)).

---

#### Disclaimers

General questions or feedback? Contact [team@carpentries.org](mailto:team@carpentries.org).

Inline HTML with `fa` tags refer to [Font Awesome](https://fontawesome.com/icons?d=gallery).
