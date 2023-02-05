#list of attractive projects in Rubuygems
rubylonglived2017=rubyMS[(rubyMS['magnet_2017']>rubyMS['magnet_2017'].median()) & (rubyMS['sticky_2017']>rubyMS['sticky_2017'].median())]
rubylonglived2018=rubyMS[(rubyMS['magnet_2018']>rubyMS['magnet_2018'].median()) & (rubyMS['sticky_2018']>rubyMS['sticky_2018'].median())]
rubylonglived2019=rubyMS[(rubyMS['magnet_2019']>rubyMS['magnet_2019'].median()) & (rubyMS['sticky_2019']>rubyMS['sticky_2019'].median())]
rubylonglived2020=rubyMS[(rubyMS['magnet_2020']>rubyMS['magnet_2020'].median()) & (rubyMS['sticky_2020']>rubyMS['sticky_2020'].median())]
len(rubylonglived2017),len(rubylonglived2018),len(rubylonglived2019),len(rubylonglived2020)
list(reduce(set.intersection, map(set, [rubylonglived2017.project, rubylonglived2018.project, rubylonglived2019.project, rubylonglived2020.project])))

#list of terminal projects in Rubygems
rubydead2017=rubyMS[(rubyMS['magnet_2017']<rubyMS['magnet_2017'].median()) & (rubyMS['sticky_2017']<rubyMS['sticky_2017'].median())]
rubydead2018=rubyMS[(rubyMS['magnet_2018']<rubyMS['magnet_2018'].median()) & (rubyMS['sticky_2018']<rubyMS['sticky_2018'].median())]
rubydead2019=rubyMS[(rubyMS['magnet_2019']<rubyMS['magnet_2019'].median()) & (rubyMS['sticky_2019']<rubyMS['sticky_2019'].median())]
rubydead2020=rubyMS[(rubyMS['magnet_2020']<rubyMS['magnet_2020'].median()) & (rubyMS['sticky_2020']<rubyMS['sticky_2020'].median())]
len(rubydead2017), len(rubydead2018),len(rubydead2019),len(rubydead2020)
list(reduce(set.intersection, map(set, [rubydead2017.project, rubydead2018.project, rubydead2019.project, rubydead2020.project])))

#list of attractive projects in PyPI
pypilonglived2017=pypiMS[(pypiMS['magnet_2017']>pypiMS['magnet_2017'].median()) & (pypiMS['sticky_2017']>pypiMS['sticky_2017'].median())]
pypilonglived2018=pypiMS[(pypiMS['magnet_2018']>pypiMS['magnet_2018'].median()) & (pypiMS['sticky_2018']>pypiMS['sticky_2018'].median())]
pypilonglived2019=pypiMS[(pypiMS['magnet_2019']>pypiMS['magnet_2019'].median()) & (pypiMS['sticky_2019']>pypiMS['sticky_2019'].median())]
pypilonglived2020=pypiMS[(pypiMS['magnet_2020']>pypiMS['magnet_2020'].median()) & (pypiMS['sticky_2020']>pypiMS['sticky_2020'].median())]
len(pypilonglived2017),len(pypilonglived2018),len(pypilonglived2019),len(pypilonglived2020)
list(reduce(set.intersection, map(set, [pypilonglived2017.project, pypilonglived2018.project, pypilonglived2019.project, pypilonglived2020.project])))

#list of terminal projects in PyPI
pypidead2017=pypiMS[(pypiMS['magnet_2017']<pypiMS['magnet_2017'].median()) & (pypiMS['sticky_2017']<pypiMS['sticky_2017'].median())]
pypidead2018=pypiMS[(pypiMS['magnet_2018']<pypiMS['magnet_2018'].median()) & (pypiMS['sticky_2018']<pypiMS['sticky_2018'].median())]
pypidead2019=pypiMS[(pypiMS['magnet_2019']<pypiMS['magnet_2019'].median()) & (pypiMS['sticky_2019']<pypiMS['sticky_2019'].median())]
pypidead2020=pypiMS[(pypiMS['magnet_2020']<pypiMS['magnet_2020'].median()) & (pypiMS['sticky_2020']<pypiMS['sticky_2020'].median())]
len(pypidead2017), len(pypidead2018),len(pypidead2019),len(pypidead2020)
list(reduce(set.intersection, map(set, [pypidead2017.project, pypidead2018.project, pypidead2019.project, pypidead2020.project])))

#list of attractive projects in npm
npmlonglived2017=npmMS[(npmMS['magnet_2017']>npmMS['magnet_2017'].median()) & (npmMS['sticky_2017']>npmMS['sticky_2017'].median())]
npmlonglived2018=npmMS[(npmMS['magnet_2018']>npmMS['magnet_2018'].median()) & (npmMS['sticky_2018']>npmMS['sticky_2018'].median())]
npmlonglived2019=npmMS[(npmMS['magnet_2019']>npmMS['magnet_2019'].median()) & (npmMS['sticky_2019']>npmMS['sticky_2019'].median())]
npmlonglived2020=npmMS[(npmMS['magnet_2020']>npmMS['magnet_2020'].median()) & (npmMS['sticky_2020']>npmMS['sticky_2020'].median())]
len(npmlonglived2017), len(npmlonglived2018),len(npmlonglived2019),len(npmlonglived2020)
list(reduce(set.intersection, map(set, [npmlonglived2017.project, npmlonglived2018.project, npmlonglived2019.project, npmlonglived2020.project])))

#list of terminal projects in npm
npmdead2017=npmMS[(npmMS['magnet_2017']<npmMS['magnet_2017'].median()) & (npmMS['sticky_2017']<npmMS['sticky_2017'].median())]
npmdead2018=npmMS[(npmMS['magnet_2018']<npmMS['magnet_2018'].median()) & (npmMS['sticky_2018']<npmMS['sticky_2018'].median())]
npmdead2019=npmMS[(npmMS['magnet_2019']<npmMS['magnet_2019'].median()) & (npmMS['sticky_2019']<npmMS['sticky_2019'].median())]
npmdead2020=npmMS[(npmMS['magnet_2020']<npmMS['magnet_2020'].median()) & (npmMS['sticky_2020']<npmMS['sticky_2020'].median())]
len(npmdead2017), len(npmdead2018),len(npmdead2019),len(npmdead2020)
list(reduce(set.intersection, map(set, [npmdead2017.project, npmdead2018.project, npmdead2019.project, npmdead2020.project])))