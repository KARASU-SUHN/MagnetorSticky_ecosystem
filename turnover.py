## ruby to npm/pypi

#ruby leave next year
ruby_2016notin2017 = ruby2016[~(ruby2016['author'].isin(ruby2017['author']))].reset_index(drop=True)
ruby_2017notin2018 = ruby2017[~(ruby2017['author'].isin(ruby2018['author']))].reset_index(drop=True)
ruby_2018notin2019 = ruby2018[~(ruby2018['author'].isin(ruby2019['author']))].reset_index(drop=True)
ruby_2019notin2020 = ruby2019[~(ruby2019['author'].isin(ruby2020['author']))].reset_index(drop=True)
ruby_2020notin2021 = ruby2020[~(ruby2020['author'].isin(ruby2021['author']))].reset_index(drop=True)

# of leave
ruby_2016notin2020 = ruby2016[~(ruby2016['author'].isin(ruby2020['author']))].reset_index(drop=True)

len(ruby_2016notin2017['author'].drop_duplicates()),len(ruby_2017notin2018['author'].drop_duplicates()),len(ruby_2018notin2019['author'].drop_duplicates()),len(ruby_2019notin2020['author'].drop_duplicates()),len(ruby_2020notin2021['author'].drop_duplicates())

#Ruby transfer to NPM
ruby_to_npm2017=pd.DataFrame(list(reduce(set.intersection, map(set, [ruby_2016notin2017.author, npm2017.author]))),columns =['same'])
ruby_to_npm2018=pd.DataFrame(list(reduce(set.intersection, map(set, [ruby_2017notin2018.author, npm2018.author]))),columns =['same'])
ruby_to_npm2019=pd.DataFrame(list(reduce(set.intersection, map(set, [ruby_2018notin2019.author, npm2019.author]))),columns =['same'])
ruby_to_npm2020=pd.DataFrame(list(reduce(set.intersection, map(set, [ruby_2019notin2020.author, npm2020.author]))),columns =['same'])
ruby_to_npm2021=pd.DataFrame(list(reduce(set.intersection, map(set, [ruby_2020notin2021.author, npm2021.author]))),columns =['same'])

##Ruby transfer to Pypi
ruby_to_pypi2017=pd.DataFrame(list(reduce(set.intersection, map(set, [ruby_2016notin2017.author, pypi2017.author]))),columns =['same'])
ruby_to_pypi2018=pd.DataFrame(list(reduce(set.intersection, map(set, [ruby_2017notin2018.author, pypi2018.author]))),columns =['same'])
ruby_to_pypi2019=pd.DataFrame(list(reduce(set.intersection, map(set, [ruby_2018notin2019.author, pypi2019.author]))),columns =['same'])
ruby_to_pypi2020=pd.DataFrame(list(reduce(set.intersection, map(set, [ruby_2019notin2020.author, pypi2020.author]))),columns =['same'])
ruby_to_pypi2021=pd.DataFrame(list(reduce(set.intersection, map(set, [ruby_2020notin2021.author, pypi2021.author]))),columns =['same'])

#number of new author from ruby to npm
len(ruby_to_npm2017.drop_duplicates()),len(ruby_to_npm2018.drop_duplicates()),len(ruby_to_npm2019.drop_duplicates()),len(ruby_to_npm2020.drop_duplicates()),len(ruby_to_npm2021.drop_duplicates())
#number of new author from ruby to pypi
len(ruby_to_pypi2017.drop_duplicates()),len(ruby_to_pypi2018.drop_duplicates()),len(ruby_to_pypi2019.drop_duplicates()),len(ruby_to_pypi2020.drop_duplicates()),len(ruby_to_pypi2021.drop_duplicates())

# ruby to NPM and Pypi
# len(list(reduce(set.intersection, map(set, [ruby_to_npm2017.same, ruby_to_pypi2017.same])))),len(list(reduce(set.intersection, map(set, [ruby_to_npm2018.same, ruby_to_pypi2018.same])))),len(list(reduce(set.intersection, map(set, [ruby_to_npm2019.same, ruby_to_pypi2019.same])))),len(list(reduce(set.intersection, map(set, [ruby_to_npm2020.same, ruby_to_pypi2020.same])))),len(list(reduce(set.intersection, map(set, [ruby_to_npm2021.same, ruby_to_pypi2021.same]))))

## npm to pypi/ruby

#npm leave next year
npm_2016notin2017 = npm2016[~(npm2016['author'].isin(npm2017['author']))].reset_index(drop=True)
npm_2017notin2018 = npm2017[~(npm2017['author'].isin(npm2018['author']))].reset_index(drop=True)
npm_2018notin2019 = npm2018[~(npm2018['author'].isin(npm2019['author']))].reset_index(drop=True)
npm_2019notin2020 = npm2019[~(npm2019['author'].isin(npm2020['author']))].reset_index(drop=True)
npm_2020notin2021 = npm2020[~(npm2020['author'].isin(npm2021['author']))].reset_index(drop=True)

# of leave
npm_2016notin2020 = npm2016[~(npm2016['author'].isin(npm2020['author']))].reset_index(drop=True)

#npm transfer to ruby
npm_to_ruby2017=pd.DataFrame(list(reduce(set.intersection, map(set, [npm_2016notin2017.author, ruby2017.author]))),columns =['same'])
npm_to_ruby2018=pd.DataFrame(list(reduce(set.intersection, map(set, [npm_2017notin2018.author, ruby2018.author]))),columns =['same'])
npm_to_ruby2019=pd.DataFrame(list(reduce(set.intersection, map(set, [npm_2018notin2019.author, ruby2019.author]))),columns =['same'])
npm_to_ruby2020=pd.DataFrame(list(reduce(set.intersection, map(set, [npm_2019notin2020.author, ruby2020.author]))),columns =['same'])
npm_to_ruby2021=pd.DataFrame(list(reduce(set.intersection, map(set, [npm_2020notin2021.author, ruby2021.author]))),columns =['same'])

##npm transfer to Pypi
npm_to_pypi2017=pd.DataFrame(list(reduce(set.intersection, map(set, [npm_2016notin2017.author, pypi2017.author]))),columns =['same'])
npm_to_pypi2018=pd.DataFrame(list(reduce(set.intersection, map(set, [npm_2017notin2018.author, pypi2018.author]))),columns =['same'])
npm_to_pypi2019=pd.DataFrame(list(reduce(set.intersection, map(set, [npm_2018notin2019.author, pypi2019.author]))),columns =['same'])
npm_to_pypi2020=pd.DataFrame(list(reduce(set.intersection, map(set, [npm_2019notin2020.author, pypi2020.author]))),columns =['same'])
npm_to_pypi2021=pd.DataFrame(list(reduce(set.intersection, map(set, [npm_2020notin2021.author, pypi2021.author]))),columns =['same'])

#number of new author from npm to ruby
len(npm_to_ruby2017.drop_duplicates()),len(npm_to_ruby2018.drop_duplicates()),len(npm_to_ruby2019.drop_duplicates()),len(npm_to_ruby2020.drop_duplicates()),len(npm_to_ruby2021.drop_duplicates())

#number of new author from npm to pypi
len(npm_to_pypi2017.drop_duplicates()),len(npm_to_pypi2018.drop_duplicates()),len(npm_to_pypi2019.drop_duplicates()),len(npm_to_pypi2020.drop_duplicates()),len(npm_to_pypi2021.drop_duplicates())

# NPM to npm and Pypi
len(list(reduce(set.intersection, map(set, [npm_to_ruby2017.same, npm_to_pypi2017.same])))),len(list(reduce(set.intersection, map(set, [npm_to_ruby2018.same, npm_to_pypi2018.same])))),len(list(reduce(set.intersection, map(set, [npm_to_ruby2019.same, npm_to_pypi2019.same])))),len(list(reduce(set.intersection, map(set, [npm_to_ruby2020.same, npm_to_pypi2020.same])))),len(list(reduce(set.intersection, map(set, [npm_to_ruby2021.same, npm_to_pypi2021.same]))))

# PyPI to npm/ruby

#pypi leave next year
pypi_2016notin2017 = pypi2016[~(pypi2016['author'].isin(pypi2017['author']))].reset_index(drop=True)
pypi_2017notin2018 = pypi2017[~(pypi2017['author'].isin(pypi2018['author']))].reset_index(drop=True)
pypi_2018notin2019 = pypi2018[~(pypi2018['author'].isin(pypi2019['author']))].reset_index(drop=True)
pypi_2019notin2020 = pypi2019[~(pypi2019['author'].isin(pypi2020['author']))].reset_index(drop=True)
pypi_2020notin2021 = pypi2020[~(pypi2020['author'].isin(pypi2021['author']))].reset_index(drop=True)

len(pypi_2016notin2017['author'].drop_duplicates()),len(pypi_2017notin2018['author'].drop_duplicates()),len(pypi_2018notin2019['author'].drop_duplicates()),len(pypi_2019notin2020['author'].drop_duplicates()),len(pypi_2020notin2021['author'].drop_duplicates())

# of leave
pypi_2016notin2020 = pypi2016[~(pypi2016['author'].isin(pypi2020['author']))].reset_index(drop=True)
len(pypi_2017notin2016['author'].drop_duplicates())

#pypi transfer to ruby
pypi_to_ruby2017=pd.DataFrame(list(reduce(set.intersection, map(set, [pypi_2016notin2017.author, ruby2017.author]))),columns =['same'])
pypi_to_ruby2018=pd.DataFrame(list(reduce(set.intersection, map(set, [pypi_2017notin2018.author, ruby2018.author]))),columns =['same'])
pypi_to_ruby2019=pd.DataFrame(list(reduce(set.intersection, map(set, [pypi_2018notin2019.author, ruby2019.author]))),columns =['same'])
pypi_to_ruby2020=pd.DataFrame(list(reduce(set.intersection, map(set, [pypi_2019notin2020.author, ruby2020.author]))),columns =['same'])
pypi_to_ruby2021=pd.DataFrame(list(reduce(set.intersection, map(set, [pypi_2020notin2021.author, ruby2021.author]))),columns =['same'])

##pypi transfer to Pypi
pypi_to_npm2017=pd.DataFrame(list(reduce(set.intersection, map(set, [pypi_2016notin2017.author, npm2017.author]))),columns =['same'])
pypi_to_npm2018=pd.DataFrame(list(reduce(set.intersection, map(set, [pypi_2017notin2018.author, npm2018.author]))),columns =['same'])
pypi_to_npm2019=pd.DataFrame(list(reduce(set.intersection, map(set, [pypi_2018notin2019.author, npm2019.author]))),columns =['same'])
pypi_to_npm2020=pd.DataFrame(list(reduce(set.intersection, map(set, [pypi_2019notin2020.author, npm2020.author]))),columns =['same'])
pypi_to_npm2021=pd.DataFrame(list(reduce(set.intersection, map(set, [pypi_2020notin2021.author, npm2021.author]))),columns =['same'])

#number of new author from pypi to ruby
len(pypi_to_ruby2017.drop_duplicates()),len(pypi_to_ruby2018.drop_duplicates()),len(pypi_to_ruby2019.drop_duplicates()),len(pypi_to_ruby2020.drop_duplicates()),len(pypi_to_ruby2021.drop_duplicates())

#number of new author from pypi to npm
len(pypi_to_npm2017.drop_duplicates()),len(pypi_to_npm2018.drop_duplicates()),len(pypi_to_npm2019.drop_duplicates()),len(pypi_to_npm2020.drop_duplicates()),len(pypi_to_npm2021.drop_duplicates())

# pypi to ruby and npm
len(list(reduce(set.intersection, map(set, [pypi_to_ruby2017.same, pypi_to_npm2017.same])))),len(list(reduce(set.intersection, map(set, [pypi_to_ruby2018.same, pypi_to_npm2018.same])))),len(list(reduce(set.intersection, map(set, [pypi_to_ruby2019.same, pypi_to_npm2019.same])))),len(list(reduce(set.intersection, map(set, [pypi_to_ruby2020.same, pypi_to_npm2020.same])))),len(list(reduce(set.intersection, map(set, [pypi_to_ruby2021.same, pypi_to_npm2021.same]))))

# random error check!
(npm2017['author'].eq('Christian Bundy <christianbundy@fraction.io>')).any()
pypi2017['author'].str.contains('Christian Bundy <christianbundy@fraction.io>').any()
# (npm2018['author'].eq('Jon Moss <maclover7@users.noreply.github.com>')).any()
# ruby2018['author'].str.contains('Jon Moss').any()
ruby2020['author'].eq('Jakub Sokołowski <jakub@status.im>').any()
npm2020['author'].str.contains('Jakub Sokołowski <jakub@status.im>').any()