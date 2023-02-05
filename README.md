# MagnetorSticky_ecosystem

## This is the replication package for MSR challenge paper: Exploring the Magnetic or Sticky Nature of GitHub Ecosystems: NPM, PyPI, and Rubygems.

### We provide all the datasets used in this paper here.

NPM100P.txt - top-100 projects in npm.\
Pypi100P.txt - top-100 projects in PyPI.\
Ruby100P.txt - top-100 projects in Rubygems.
#### clean_data.zip contain npm_clean.txt, pypi_clean.txt, ruby_clean.txt
npm_clean.txt- the projects, commits, dates, and authors of npm during 2016-2021.\
pypi_clean.txt- the projects, commits, dates, and authors of PyPI during 2016-2021.\
ruby_clean.txt- the projects, commits, dates, and authors of Rubygems during 2016-2021.

ecosystemMS.csv - the magnet and sticky values of each ecosystem in 2017-2020.\
domain_result.csv - the domain of 300 projects, and the magnet and sticky values of each project in 2017-2020.\
Ecosystem_cross.csv - the number of authors cross in the three ecosystems(i.e., npm, PyPI and Rubygems) during 2017-2020.\
Attractive_terminal.csv - the attractive and terminal projects with the number of commits in the past year. \
dormant.txt -  the list of attractive, terminal, and dormant projects.
#### code
woc.py - our data prepartion process in WoC da0 server.\
contributor.py - calulate the number of contributers in each ecosystem.\
turnover.py - ecosystem cross.\
attractive_or_terminal.py - extract all attractive and terminal projects.
