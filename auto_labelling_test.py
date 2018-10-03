import unittest
import auto_labelling

class TestAutoLabelling(unittest.TestCase):
    def test_find_csv_file(self):
        self.assertEqual(auto_labelling._find_csv_file(), './data/PepitoTheCat-140801102068195328(20111127_153613)-1004221040485158912(20180606_063848)-media/PepitoTheCat-140801102068195328(20111127_153613)-1004221040485158912(20180606_063848)-media.csv')

    def test_label_images(self):
        df = auto_labelling._label_images(auto_labelling._find_csv_file())

        df = df[(df['img_name'] == 'PepitoTheCat-304824772993368066-20130222_062744-img1.jpg') 
                | (df['img_name'] == 'PepitoTheCat-313165014880096257-20130317_064852-img1.jpg') 
                | (df['img_name'] == 'PepitoTheCat-912581058268459008-20170926_093413-img1.jpg')
                | (df['img_name'] == 'PepitoTheCat-592840672949993473-20150428_020005-img1.jpg')]

        self.assertTrue(
                df[(df['img_name'] == 'PepitoTheCat-304824772993368066-20130222_062744-img1.jpg') 
                | (df['img_name'] == 'PepitoTheCat-912581058268459008-20170926_093413-img1.jpg')
                | (df['img_name'] == 'PepitoTheCat-592840672949993473-20150428_020005-img1.jpg')]
                .equals(
                    df[df['label'] == 'home']
                )            
        )

        self.assertTrue(
                df[df['img_name'] == 'PepitoTheCat-313165014880096257-20130317_064852-img1.jpg']
                .equals(
                    df[df['label'] == 'out']
                )            
        )        

        # 'PepitoTheCat-304824772993368066-20130222_062744-img1.jpg', 'home'
        # 'PepitoTheCat-313165014880096257-20130317_064852-img1.jpg', 'out'
        # 'PepitoTheCat-912581058268459008-20170926_093413-img1.jpg', 'home'
        # 'PepitoTheCat-592840672949993473-20150428_020005-img1.jpg', 'home'

    # def test_auto_labelling(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()