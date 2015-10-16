# coding : utf-8
__author__ = 'zsh'
import re

tihuan = re.compile('<.*?>')

b = tihuan.sub('', '<><><><>asdf<p>asdf<><><>')
print(b)

a = 'Foreachcaseoutputthesumofallthei-Matrix(0<=i<=k)innlines.Eachlinetherearenintegersseparatedbyonespace.Notethatthereisnoextraspaceattheendofeachline.      Attention:forthelargestdate,you&lsquo;dbetterusethetypeoflonglongtoouputyouranswer'
a = a.replace(' ', '')
print(a)
