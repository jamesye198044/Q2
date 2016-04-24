#!/usr/bin/python

import unittest
from fib_restful import fib_list
import requests


class Q2_UnitTest(unittest.TestCase):

    def test_short_fiblist(self):

        result = fib_list(5)
        self.assertEquals(result[4],3)
        self.assertEquals(len(result),5)

    def test_0_fiblist(self):

        result = fib_list(0)
        self.assertEquals(result[0],0)
        self.assertEquals(len(result),1)


    def test_1_fiblist(self):

        result = fib_list(1)
        self.assertEquals(result[0],0)
        self.assertEquals(len(result),1)

    def test_2_fiblist(self):

        result = fib_list(2)
        self.assertEquals(result[0],0)
        self.assertEquals(result[1],1)
        self.assertEquals(len(result),2)

    def test_long_fiblist(self):

         result = fib_list(10000)
         number = 20793608237133498072112648988642836825087036094015903119682945866528501423455686648927456034305226515591757343297190158010624794267250973176133810179902738038231789748346235556483191431591924532394420028067810320408724414693462849062668387083308048250920654493340878733226377580847446324873797603734794648258113858631550404081017260381202919943892370942852601647398213554479081823593715429566945149312993664846779090437799284773675379284270660175134664833266377698642012106891355791141872776934080803504956794094648292880566056364718187662668970758537383352677420835574155945658542003634765324541006121012446785689171494803262408602693091211601973938229446636049901531963286159699077880427720289235539329671877182915643419079186525118678856821600897520171070499437657067342400871083908811800976259727431820539554256869460815355918458253398234382360435762759823179896116748424269545924633204614137992850814352018738480923581553988990897151469406131695614497783720743461373756218685106856826090696339815490921253714537241866911604250597353747823733268178182198509240226955826416016690084749816072843582488613184829905383150180047844353751554201573833105521980998123833253261228689824051777846588461079790807828367132384798451794011076569057522158680378961532160858387223882974380483931929541222100800313580688585002598879566463221427820448492565073106595808837401648996423563386109782045634122467872921845606409174360635618216883812562321664442822952537577492715365321134204530686742435454505103269768144370118494906390254934942358904031509877369722437053383165360388595116980245927935225901537634925654872380877183008301074569444002426436414756905094535072804764684492105680024739914490555904391369218696387092918189246157103450387050229300603241611410707453960080170928277951834763216705242485820801423866526633816082921442883095463259080471819329201710147828025221385656340207489796317663278872207607791034431700112753558813478888727503825389066823098683355695718137867882982111710796422706778536913192342733364556727928018953989153106047379741280794091639429908796650294603536651238230626
         self.assertEquals(result[9999], number)
         self.assertEquals(len(result),10000)

    def test_negative_fiblist(self):

        result = fib_list(-1)
        self.assertEquals(result,'Error, must be greater than or equal to 0 and must be a integer')

    def test_float_fiblist(self):

        result = fib_list(5.5)
        self.assertEquals(result,'Error, n must be integer')


    def test_listusage(self):

        response = requests.get('http://127.0.0.1:8080/fib')
        self.assertIn('Fibonacci service usage is as below example',response.content)
        self.assertEquals(200,response.status_code)

class Q2_FunctionTest(unittest.TestCase):

    def test_getnumber_5(self):

        response = requests.get('http://127.0.0.1:8080/fib/5')
        self.assertIn('[0, 1, 1, 2, 3]',response.content)
        self.assertEquals(200,response.status_code)

    def test_getnumber_0(self):

        response = requests.get('http://127.0.0.1:8080/fib/0')
        self.assertIn('[0]',response.content)
        self.assertEquals(200,response.status_code)

    def test_getnumber_1(self):

        response = requests.get('http://127.0.0.1:8080/fib/0')
        self.assertIn('[0]',response.content)
        self.assertEquals(200,response.status_code)

    def test_getnumber_2(self):

        response = requests.get('http://127.0.0.1:8080/fib/2')
        self.assertIn('[0, 1]',response.content)
        self.assertEquals(200,response.status_code)

    def test_getnumber_negative(self):

        response = requests.get('http://127.0.0.1:8080/fib/-1')
        self.assertIn('Error, must be greater than or equal to 0 and must be a integer',response.content)
        self.assertEquals(200,response.status_code)


    def test_getnumber_float(self):

        response = requests.get('http://127.0.0.1:8080/fib/3.3')
        self.assertIn('Error, must be greater than or equal to 0 and must be a integer',response.content)
        self.assertEquals(200,response.status_code)


    def test_getnumber_letter(self):

        response = requests.get('http://127.0.0.1:8080/fib/aaa')
        self.assertIn('Error, must be greater than or equal to 0 and must be a integer',response.content)
        self.assertEquals(200,response.status_code)

    def test_multi_slash1(self):

        response = requests.get('http://127.0.0.1:8080/fib/5//')
        self.assertIn('Error, must be greater than or equal to 0 and must be a integer',response.content)
        self.assertEquals(200,response.status_code)


    def test_multi_slash2(self):

        response = requests.get('http://127.0.0.1:8080/fib///')
        self.assertIn('Error, must be greater than or equal to 0 and must be a integer',response.content)
        self.assertEquals(200,response.status_code)

    def test_getnumber_long(self):

        number = '20793608237133498072112648988642836825087036094015903119682945866528501423455686648927456034305226515591757343297190158010624794267250973176133810179902738038231789748346235556483191431591924532394420028067810320408724414693462849062668387083308048250920654493340878733226377580847446324873797603734794648258113858631550404081017260381202919943892370942852601647398213554479081823593715429566945149312993664846779090437799284773675379284270660175134664833266377698642012106891355791141872776934080803504956794094648292880566056364718187662668970758537383352677420835574155945658542003634765324541006121012446785689171494803262408602693091211601973938229446636049901531963286159699077880427720289235539329671877182915643419079186525118678856821600897520171070499437657067342400871083908811800976259727431820539554256869460815355918458253398234382360435762759823179896116748424269545924633204614137992850814352018738480923581553988990897151469406131695614497783720743461373756218685106856826090696339815490921253714537241866911604250597353747823733268178182198509240226955826416016690084749816072843582488613184829905383150180047844353751554201573833105521980998123833253261228689824051777846588461079790807828367132384798451794011076569057522158680378961532160858387223882974380483931929541222100800313580688585002598879566463221427820448492565073106595808837401648996423563386109782045634122467872921845606409174360635618216883812562321664442822952537577492715365321134204530686742435454505103269768144370118494906390254934942358904031509877369722437053383165360388595116980245927935225901537634925654872380877183008301074569444002426436414756905094535072804764684492105680024739914490555904391369218696387092918189246157103450387050229300603241611410707453960080170928277951834763216705242485820801423866526633816082921442883095463259080471819329201710147828025221385656340207489796317663278872207607791034431700112753558813478888727503825389066823098683355695718137867882982111710796422706778536913192342733364556727928018953989153106047379741280794091639429908796650294603536651238230626'
        response = requests.get('http://127.0.0.1:8080/fib/10000')
        self.assertIn(number,response.content)
        self.assertEquals(200,response.status_code)