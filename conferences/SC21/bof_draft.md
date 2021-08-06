# Title: HPC Carpentry: Introducing New Users to HPC

## Session Leaders

Andrew Reid
: he/him. Computer operations administrator for the [CTCMS][ctcms]
  clusters at [NIST][nist], managing a rotating cast of cluster
  users of varying levels of experience. Also materials scientist
  and co-developer of the [OOF][oof] finite-element tool,
  facilitating structure-property exploration for other materials
  scientists. On GitHub [@reid-a][reid-a].

Trevor Keller
: they/them. Materials research engineer at [NIST][nist] and inchoate
  systems administrator for the [CTCMS][ctcms] clusters, specializing in
  solid-state transformations in additively manufactured metals and
  filesystem frustrations in parallel. On GitHub [@tkphd][tkphd].

Alan O'Cais
: he/him. Software Manager of E-CAM, an EU Centre of Excellence in
  HPC computing applications. Previously managed the user software and
  application environment on the multi-PFlop JURECA hybrid cluster
  system. On GitHub [@ocaisa][ocaisa].

Annajiat Alim Rasel
: he/him. Learner of Parallel, Distributed, and High Performance
  Computing (HPC), and Sr. Lecturer at the School of Data and Sciences
  at Brac University. On GitHub [@anajiat][annajiat].

## Topic Area

- Education

## Abstract:

[HPC Carpentry][1] introduces new users to high-performance computing
through a set of community-contributed lessons. As diverse and powerful
hardware becomes more widely deployed, users from a variety of technical
backgrounds are faced with the challenge of adapting their problems
to new environments; educational resources to bring users up to speed
become more significant. Based on the approach of [The Carpentries][2],
HPC Carpentry lessons in development include an [introduction][3] to the
use of a queuing system and an introduction to [parallel programming
in Python][4]. The introductory lesson is part of the [Incubator][7],
where it benefits from the broader Carpentries community.

## Long description:

### Who we are

The [HPC Carpentry][1] community, a volunteer group of high-performance
computing practitioners led by a [steering committee][6], has developed
a number of introductory lessons for new users of HPC systems.

### What problem we solve

Greater computational capabilities are becoming increasingly
affordable. An under-appreciated consequence of this is that the range
of backgrounds of new users of these resources is increasingly broad,
and may not include knowledge of computer system configurations and
file system layouts. This prevents users from making effective use of
these new systems. There is an evident on-going need to address the
gap between the skills and expectations of users and the capabilities
and opportunities presented by the available HPC resources.

The [HPC Carpentry][1] lessons address this gap, building on the
pedagogically sound instructional methods of the larger [Carpentries][2]
community. The best-developed lesson, [HPC Intro][3], was recently
submitted to the [Carpentries Incubator][7], where it benefits from
input from the broader Carpentries audience. Another important lesson
in development uses Python and MPI to introduce the basics of
[parallel programming][4].

Many of our community members have important operational experience with
a variety of HPC tools in a pedagogical context, including the design,
procurement, deployment, and maintenance of on-premise hardware,
container, and cloud systems. This informs the lesson-development
process at many levels.

### Goals for the BoF

During this BoF, we will gather community feedback on our progress to
date, to ensure that we are helping HPC operators bring users on board,
and helping users make good use of the systems. This will help the HPC
Carpentry development team prioritize efforts for successor lessons in
light of the changing landscape of current HPC practice.

We plan discuss the following strategic topics:

1. For people who have used existing HPC Carpentry material, we are
   interested in positive and negative aspects of the experience.

    - Were HPC Carpentry lessons used exclusively, or in combination
      with material from The Carpentries or elsewhere?
    - What sequence of lessons was used to build the workshop?

2. Our existing lessons are not uniformly developed, and we have many
   good ideas for future lessons. Which to prioritize?

    - Existing lessons cover the important topics. Effort should go to
      improving them.
    - Higher-level programming languages: Chapel, Julia, Python.
    - Lower-level programming languages: C, CUDA, Fortran, OpenMP.
    - HPC frameworks -- Containers, Dask, Kokkos, MPI, parallel CUDA.

3. Should the lessons be teachable as stand-alone sessions, with
   resultant overlap of material, or should the lessons form a "deck"
   that workshop coordinators can mix and match?

4. How should we use existing complementary materials? There are
   resources available on some of our aspirational topics (containers,
   Julia, security). Should we:

    - Directly insert external lessons into workshops?
    - "Fork" and adapt external materials for our purposes?
    - Only present lessons we have written ourselves?

5. The current HPC Intro lesson has templates for customization to local
   resources. There is obvious tension between having flexible templates
   versus ease of set-up.

    - How much templating is useful?
    - Is the current degree of templating burdensome?
    - Should the material be adapted to permanent on-premise resources,
      or transient cloud resources?

6. What duration of workshop is practical for teaching this material?

    - One 3-hour session (half-day)?
    - Two 3-hour sessions (full day)?
    - Three 3-hour sessions (one-and-a-half day)?
    - Four 3-hour sessions (two full days)?

## Interactivity

Approximately 3/4 of the session will be interactive, polling the
audience on the questions above.

## Format of the non-audience-participation portion

25 minutes of presentations by the session leaders, with slides or
online visual content.

## Commercial?

No.

## Format

The BoF will open with a presentation of the current state of the
lessons, including "pain points" identified by the development team,
after which an open discussion will be held to solicit feedback on these
points, and the questions above, from the attendees.

## Prior BoFs?

An HPC Carpentry BoF was held at SC17, and an informal group of about
fifteen participants got together at SC18.

## Time, expected attendance, keywords

- We expect the session will last 1.5 hours.
- We expect around 50 participants.
- Carpentries, carpentry, education, new users

## Website link:

[HPC Carpentry][1].

<!-- References follow on -->

[1]: https://hpc-carpentry.org
[2]: https://carpentries.org
[3]: https://github.com/carpentries-incubator/hpc-intro
[4]: https://github.com/hpc-carpentry/hpc-parallel-novice
[5]: https://github.com/hpc-carpentry/hpc-chapel
[6]: http://www.hpc-carpentry.org/contact/
[7]: https://github.com/carpentries-incubator

[nist]: https://www.nist.gov
[ctcms]: https://www.ctcms.nist.gov
[oof]: https://www.ctcms.nist.gov/oof/

[annajiat]: https://github.com/annajiat
[ocaisa]:   https://github.com/ocaisa
[reid-a]:   https://github.com/reid-a
[tkphd]:    https://github.com/tkphd
