# HPCC Coworking Hours: 1 April 2021

The HPC Carpentries Task Force holds coworking hours on the first Thursday,
with two time slots intended to provide adequate coverage for our global
constituency. Check your local times below, and join whichever is most 
convenient. See you soon!

<!-- Important links to define, placed up top for convenience -->
[earlier]: https://www.timeanddate.com/worldclock/fixedtime.html?iso=20210401T1200&msg=HPC+Carpentries+Coworking+Hour+1
[evening]: https://www.timeanddate.com/worldclock/fixedtime.html?iso=20210401T2200&msg=HPC+Carpentries+Coworking+Hour+2
[last-cowork]: https://codimd.carpentries.org/Df6SsurcSzuhChlhNwqdHw?view
[last-coord]: https://codimd.carpentries.org/5zpJN7jZQ_SChBWz2bvKVg?view

#### Check your local times

:::danger
**Daylight Saving Time** has begun. Please double-check your local times.
:::

These two meeting times provide the least-painful coverage for the six
non-polar continents. Folks in Antarctica and aboard a space station
are invited to join whichever is most convenient 😉

* [12:00 UTC][earlier] &mdash; better for Africa, Asia, and Europe
* [22:00 UTC][evening] &mdash; better for the Americas and Australia

### Virtual Venue

Both meetings will use [Google Meet -URL redacted-].

### Callbacks to Previous Meetings

- [Previous Coworking Hour][last-cowork]
- [Previous Coordination Meeting][last-coord]
- Archive of old [Minutes][minutes]

---

## Earlier Meeting (Africa, Asia, and Europe)

### Participants

* Trevor Keller (he/they), NIST
* Annajiat Alim Rasel (he/him), Brac University
* Benson Muite (he/him)
* Andrew Reid (he/him) NIST

### Agenda & Minutes

#### Scheduling

An executive decision has been made, based on the recent tempo and lack of complaints, to set fixed times for HPC Carpentry meetings.

* Coworking Hours are held on the first Thursday of each month.
* Coordination Meetings are on the third Thursday of each month.

A Google calendar has been set up to capture these events, available [online](https://calendar.google.com/calendar/?cid=bWp0ZWh0ZmEycmVjZGZtNmZjdGUwMWVhdGNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ) or as an [ical file](https://github.com/hpc-carpentry/coordination/files/6240223/hpc-carpentry.ical.zip).

* [name=Annajiat] reports that the shared calendar is helpful, since the calendar app handles the time zone & DST conversions.

#### Branching Workflows

Trevor Keller will lead a discussion on branching with Git and GitHub.

##### References

* https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
* https://coderefinery.github.io/git-intro/06-branches/
* https://coderefinery.github.io/git-intro/
* https://coderefinery.github.io/git-branch-design/

##### Notes

* [name=Benson]: Is it possible for default behavior in web interface when clicking "improve this web page" to create a branch if the repository has not been forked before?
    * [name=Trevor]: Probably not, this would be GitHub-level.
* DESIRED: Make the website merge option to a branch and then make a pull request only
* [name=Benson]: Creating tools such as used in http://datasift.github.io/gitflow is too complicated for current use case.

---

## Later Meeting (Americas & Australia)

### Participants

* Trevor Keller (he/they), NIST
* Annajiat Alim Rasel (he, him), Brac University
* Mike Renfro, Tennessee Tech
* Jon Guyer (he/him), NIST
* Andrew Reid (he/him) NIST

### Agenda & Minutes

#### Scheduling

An executive decision has been made, based on the recent tempo and lack of complaints, to set fixed times for HPC Carpentry meetings.

* Coworking Hours are held on the first Thursday of each month.
* Coordination Meetings are on the third Thursday of each month.

A Google calendar has been set up to capture these events, available [online](https://calendar.google.com/calendar/?cid=bWp0ZWh0ZmEycmVjZGZtNmZjdGUwMWVhdGNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ) or as an [ical file](https://github.com/hpc-carpentry/coordination/files/6240223/hpc-carpentry.ical.zip).

#### Branching Workflows

Trevor Keller will lead a discussion on branching with Git and GitHub.

References:

* https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
* https://coderefinery.github.io/git-intro/06-branches/
* https://coderefinery.github.io/git-intro/
* https://coderefinery.github.io/git-branch-design/


##### *Some incomplete notes*

(Presenting from [_The Pro Git_ Book](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging))

* `gh-pages` branch in hpc-carpentry lessons is equivalent to the `master` branch discussed in the chapter above.

In our lessons, when a person hits "Improve this lesson" button on the lesson website, it will direct the person to create a fork of the lesson on his/her own repo.

Desired practice:

* Preserve the main repo's `gh-pages` for changesets that have been vetted by at least one other person other than the change's author.

* When making changes
* 

Mentioned: Github Flow + other things

https://guides.github.com/introduction/flow/

http://datasift.github.io/gitflow

https://nvie.com/posts/a-successful-git-branching-model/

https://github.com/edx/edx-platform/wiki/How-to-Rebase-a-Pull-Request

**Question**: "[Is] there any way to fix all the conflict's in the [Mike]'s version through the web interface?" I.e. the commit that already diverges & conflicts with main repo -- can't do the PR on the web?

Ref: issue #336, https://github.com/carpentries-incubator/hpc-intro/pull/336

* [name=Trevor]: No, fixing this requires detaching the `HEAD` from Mike's `gh-pages` branch, moving back one commit to the consistent state, and blowing away the erroneous commit. The way to fix it on GitHub is to delete the entire repository and fork anew. On the command line, there are tools -- best bet is to find an older clone of the repo on your local machine and force-push to the fork: `git push -f my_fork gh-pages`. This will entirely overwrite the branch, but will save the rest of the repository from damage. This is important if, as is the case with Mike, there are branches representing work in progress that would be lost from GitHub.

**Question**: if we don't create a new branch initially and before creating PR, would renaming the branch be fine?

Answer: In brief, yes. But by renaming this, you will lose your `gh-pages` and it will take effort to recover that.
(You can recover from mistakes like this, but some of them may take a lot of effort--and some may require working with the local repo via CLI.)


---


<!--HPC Carpentry References-->
[coordination]: https://github.com/hpc-carpentry/coordination
[minutes]: https://github.com/hpc-carpentry/coordination/tree/main/minutes
[website]: https://github.com/hpc-carpentry/hpc-carpentry.github.io

[hpc-chapel]: https://github.com/hpc-carpentry/hpc-chapel
[hpc-intro]: https://github.com/carpentries-incubator/hpc-intro
[hpc-parallel]: https://github.com/hpc-carpentry/hpc-parallel-novice
[hpc-python]: https://github.com/hpc-carpentry/hpc-python
[hpc-shell]: https://github.com/hpc-carpentry/hpc-shell

<!--Carpentries References-->
[conduct]: https://docs.carpentries.org/topic_folders/policies/code-of-conduct.html
[invite]: https://swc-slack-invite.herokuapp.com/
[license]: https://creativecommons.org/licenses/by/4.0/
[slack]: https://swcarpentry.slack.com
