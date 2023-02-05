##Rubygems

ruby2021 = ruby_clean[ruby_clean["unix"] == 2021]
ruby2020 = ruby_clean[ruby_clean["unix"] == 2020]
ruby2019 = ruby_clean[ruby_clean["unix"] == 2019]
ruby2018 = ruby_clean[ruby_clean["unix"] == 2018]
ruby2017 = ruby_clean[ruby_clean["unix"] == 2017]
ruby2016 = ruby_clean[ruby_clean["unix"] == 2016]

#number of authors in each year
len(ruby2016['author'].drop_duplicates()),len(ruby2017['author'].drop_duplicates()),len(ruby2018['author'].drop_duplicates()),len(ruby2019['author'].drop_duplicates()),len(ruby2020['author'].drop_duplicates()),len(ruby2021['author'].drop_duplicates())

rubyincrese2021 = ruby2021[~(ruby2021['author'].isin(ruby2020['author']))].reset_index(drop=True)
rubyincrese2020 = ruby2020[~(ruby2020['author'].isin(ruby2019['author']))].reset_index(drop=True)
rubyincrese2019 = ruby2019[~(ruby2019['author'].isin(ruby2018['author']))].reset_index(drop=True)
rubyincrese2018 = ruby2018[~(ruby2018['author'].isin(ruby2017['author']))].reset_index(drop=True)
rubyincrese2017 = ruby2017[~(ruby2017['author'].isin(ruby2016['author']))].reset_index(drop=True)
author2021=rubyincrese2021['author'].drop_duplicates()
author2020=rubyincrese2020['author'].drop_duplicates()
author2019=rubyincrese2019['author'].drop_duplicates()
author2018=rubyincrese2018['author'].drop_duplicates()
author2017=rubyincrese2017['author'].drop_duplicates()
#Number of increase authors
len(author2017),len(author2018),len(author2019),len(author2020),len(author2021)

##PyPI

pypi2021 = pypi_clean[pypi_clean["unix"] == 2021]
pypi2020 = pypi_clean[pypi_clean["unix"] == 2020]
pypi2019 = pypi_clean[pypi_clean["unix"] == 2019]
pypi2018 = pypi_clean[pypi_clean["unix"] == 2018]
pypi2017 = pypi_clean[pypi_clean["unix"] == 2017]
pypi2016 = pypi_clean[pypi_clean["unix"] == 2016]

#number of authors in each year
len(pypi2016['author'].drop_duplicates()),len(pypi2017['author'].drop_duplicates()),len(pypi2018['author'].drop_duplicates()),len(pypi2019['author'].drop_duplicates()),len(pypi2020['author'].drop_duplicates()),len(pypi2021['author'].drop_duplicates())

pypiincrese2021 = pypi2021[~(pypi2021['author'].isin(pypi2020['author']))].reset_index(drop=True)
pypiincrese2020 = pypi2020[~(pypi2020['author'].isin(pypi2019['author']))].reset_index(drop=True)
pypiincrese2019 = pypi2019[~(pypi2019['author'].isin(pypi2018['author']))].reset_index(drop=True)
pypiincrese2018 = pypi2018[~(pypi2018['author'].isin(pypi2017['author']))].reset_index(drop=True)
pypiincrese2017 = pypi2017[~(pypi2017['author'].isin(pypi2016['author']))].reset_index(drop=True)
author2021=pypiincrese2021['author'].drop_duplicates()
author2020=pypiincrese2020['author'].drop_duplicates()
author2019=pypiincrese2019['author'].drop_duplicates()
author2018=pypiincrese2018['author'].drop_duplicates()
author2017=pypiincrese2017['author'].drop_duplicates()
#Number of increase authors
len(author2017),len(author2018),len(author2019),len(author2020),len(author2021)

## npm

npm2021 = npm_clean[npm_clean["unix"] == 2021]
npm2020 = npm_clean[npm_clean["unix"] == 2020]
npm2019 = npm_clean[npm_clean["unix"] == 2019]
npm2018 = npm_clean[npm_clean["unix"] == 2018]
npm2017 = npm_clean[npm_clean["unix"] == 2017]
npm2016 = npm_clean[npm_clean["unix"] == 2016]

#number of authors in each year
len(npm2016['author'].drop_duplicates()),len(npm2017['author'].drop_duplicates()),len(npm2018['author'].drop_duplicates()),len(npm2019['author'].drop_duplicates()),len(npm2020['author'].drop_duplicates()),len(npm2021['author'].drop_duplicates())

npmincrese2021 = npm2021[~(npm2021['author'].isin(npm2020['author']))].reset_index(drop=True)
npmincrese2020 = npm2020[~(npm2020['author'].isin(npm2019['author']))].reset_index(drop=True)
npmincrese2019 = npm2019[~(npm2019['author'].isin(npm2018['author']))].reset_index(drop=True)
npmincrese2018 = npm2018[~(npm2018['author'].isin(npm2017['author']))].reset_index(drop=True)
npmincrese2017 = npm2017[~(npm2017['author'].isin(npm2016['author']))].reset_index(drop=True)
author2021=npmincrese2021['author'].drop_duplicates()
author2020=npmincrese2020['author'].drop_duplicates()
author2019=npmincrese2019['author'].drop_duplicates()
author2018=npmincrese2018['author'].drop_duplicates()
author2017=npmincrese2017['author'].drop_duplicates()
#Number of increase authors
len(author2017),len(author2018),len(author2019),len(author2020),len(author2021)
