# Task Force Meeting: September 2020

We plan to meet on September 16, 2020 at 9:00 PM UTC
(11:00 PM Central Europe / 5:00 PM Eastern US / 2:00 PM Pacific US)

- [Check your local time](https://www.timeanddate.com/worldclock/fixedtime.html?iso=20200916T2100&msg=HPC%20Carpentry%20-%20Task%20Force%20Meeting:%20September%202020)
- [Join the Zoom meeting](https://us02web.zoom.us/j/84058724130)
- [Edit the shared notes (CodiMD)]( https://codimd.carpentries.org/ct7yfc_LSseoC8mEmbVEiQ?both)

## Stay connected / Check-in (optional)

- Peter Steinbach / he/him/his / twitter: @psteinb_ github: @psteinb email: p.steinbach@hzdr.de
- Toby Hodges / he/him/his / twitter: @tbyhdgs | github: tobyhodges | email: tobyhodges@carpentries.org
- Andrew Reid / he/him  / andrew.reid@nist.gov / @reid-a (github), @reid_ac (twitter) / UTC-4
- Anna Dabrowski, Texas Advanced Computing Center / she/her / email: adabrowski@tacc.utexas.edu github: @ajdabrowski
- Alan O'Cais / he/him / email: a.ocais@fz-juelich.de
- Clark Gaylord, George Washington University / he/him / cgaylord@gwu.edu / UTC-4
- Colin Sauze / he/him / email: cos@aber.ac.uk / UTC + 1
- Sabry Razick/he/github @sabryr: email sabryr@gmail.com
- Bob Freeman | he/him/his | twitter: @devbizinfoguy | github: @devbioinfoguy | email: rfreeman@hbs.edu | UTC -4
- Wirawan Purwanto | he/him | email: wpurwant@odu.edu | UTC-4
- Xiaohu Guo | he/him | email: xiaohu.guo@stfc.ac.uk | GMT
- Annajiat Alim Rasel | hi/him | email: annajiat@gmail.com | GMT+6

Apologies:
- Evgenij Belikov, EPCC | he/him | e.belikov@epcc.ed.ac.uk | UTC + 1
## Agenda

* Carpentries Liaison Toby Hodges

  - Curriculum development
  - Official liason with Carpentries core team
  - Will try to attend these meetings
  - Encourage people to get in touch

* Regular coordination meetings
  * Deciding on a date and time for regular meetings
    * Many timezones represented
      * GMT/BST (UTC/UTC+1)
      * CET/CEST (UTC+1/+2)
      * GMT/GMT+1
      * US EST/EDT (UTC-4,UTC-5)
      * US CDT/CST (UTC-5,UTC-6)
      * BDT (UTC+6)
    * 2 meetings on same day in different timezones?
      * Need overlap meeting for leaders of both
      * Good initial setup?
        * Proposal
          * 7am UTC (9am CEST)
            * Led by Peter next time out
          * something around 21:00/22:00 UTC [should be okay](https://www.timeanddate.com/worldclock/meetingtime.html?year=2020&month=9&day=17&p1=224&p2=240&p3=179) for USA+Australasia
            * Led by Andrew/Trevor
          * Get leaders together to decide a date 

    * Alternating meetings
      * Would need higher frequency
  * Which meeting tool?
    * TBD
  * Communication channels
      * Slack is an option
        * Channel is https://swcarpentry.slack.com/archives/CEXAZR52T
        * Join link for Carpentries Slack: https://swc-slack-invite.herokuapp.com/



* Updates on lesson development
  * Is hpc-intro ready for a beta release? [#174](https://github.com/hpc-carpentry/hpc-intro/issues/174)

    * Lots of issues opened (and cleared) in the last few months
    * Still a few issues
      * Added an MPI example, would like feedback
        * Has a lot going on that we don't explain
    * It still needs to be taught a bit since the changes
      * Prepare feedback session from people who have given it
      * Field testing and feedback loop
        * Who is material for?
          * Do [learner profiles](https://hpc-carpentry.github.io/why-hpc-carpentry) need updating
        * Motivate people to report feedback from these lessons (psteinb: do this in the [coordination repo](https://github.com/hpc-carpentry/coordinations))
        * Things to keep track of when "alpha testing" lessons:
            - amount of time used to teach each section
            - amount of time used for each exercise
            - technical issues that arose during installation
            - bugs or parts of the lesson code that didn’t work as expected
            - incorrect or missing exercise solutions
            - questions learners asked (and their answers)
            - parts of the lesson that were confusing for learners
            (from the [Curriculum Development Handbook](https://cdh.carpentries.org))
    * What is the timeline for the lesson pilot workshops?
        * HPC Intro is ready to be taught (alpha/beta stage)


    * What about a project board on GitHub?
        * Currently we have information in a lot of different places (need to consolidate channels!)
        * Github does have a wiki we can enable
        * Feedback questions (see above) + brief description of audience
    * Do we need to do anything required by the Carpentries?
    * Establish community processes to keep the materials long-lived
       * Shape the entire community?
 

   * New lesson plans/proposals
     * Interest from EPCC
     * Working on a lesson for LAMMPS => running code at scale. Will touch parallel computing aspects on the surface (e.g. cover threads, communications, etc but not how MPI or OpenMP really works)

     * For now, focus and consolidate on our existing lessons
       * In the future can affiliate lessons from the community on a separate "community contributed" lessons


* Task Force modus operandi (initial suggestions in brackets)
  * Initial discussion in https://github.com/hpc-carpentry/coordination/issues/12
  * Lifetime (3 months, renewable)
      * to establish community processes to develop & maintain material
      * get the HPC Carpentry material into shape
      * review after 3 months
      * first review: Christmas 2020
  * Minimum/maximum sizes (1/4)
    * 6 to 8 seems more likely given what we have seen so far
    * how much time each of us can commit?
    * Try to establish co-working hours => work on issues, etc for 60-90 mins
      * Experience tells us people only have small amounts of time to contribute
      * Small scale, weekly
  * Where to define main task (Milestone in repo)
    * Subtasks (issues and PRs)
    * Do we want to use Milestones or Github projects (linked to issues)
      * Can someone give us a demo? Sabry? (please suggest a date), OK. e.g. https://github.com/orgs/coderefinery/projects/6. 
  * Time commitment (co-working time of 1 hour a week)
    * keep track of co-working progress in a central codimd (or similar) document
    * go with a bimodal model as well for this co-working hour
        * one per week
        * 1 for US+EMEA
        * 1 for EMEA+ASIA/Australia
        
* Task definitions and volunteers
  * Potential tasks
    * Diversity
        * Need code of conduct
          * Need to officially adopt the Carpentries CoC 
        * Could reach out for help with communities already working on diversity in HPC
        * Could ideate further on tasks that would help with this goal.
          * HPC is historically very homogeneous
            * Not sure how to facilitate this
          * Get the feel how the materials are taken by different communities
          * Draw contributors from different communities
          * Example communities: Women in HPC (Peter is in contact with Lorna Rivera), 
            
    * Carpentries incubator
        * forming a new lesson set in Carpentries
        * Downside: path to the repository changes twice
          * First change: from hpc-carpentry to incubator
          * Would change again if the lesson is accepted to become formal Carpentry lesson
        * Instructors who are doing checkout can also help contribute to lessons in the incubator
        * when you're ready, open an Issue (one per lesson repository) at https://github.com/carpentries-incubator/proposals/
    * GitHub triage
    * Updating the landing page
    * Road-testing the lessons
        * put together a system to gather feedback
        * review the feedback and act on it

* AOB
  * Going forward:
    * Anything catches your eyes from this meeting => open an issue
      * Open the issue in https://github.com/hpc-carpentry/coordination for now, we can always transfer the issue to another (more appropriate) repo later 

---

General questions or feedback? Contact [team@carpentries.org](mailto:team@carpentries.org).
