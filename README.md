# NLP_processingTools
2021-09-09
****

대량의 리뷰 데이터를 다루면서 자주 필요한 툴들을 담아둡니다.  
1. data_utils.load_txt: 'csv', 'tsv' 파일에서 카테고리와 리뷰텍스트를 dict 형태로 로드합니다.
2. data_utils.cut_tsv: txt 파일을 불러와서 cut: int 단위로 쪼개 txt 파일로 출력합니다.
3. custom_tokenizer.Custom_Tokenizer: 리뷰 데이터:List[int]를 mecab, khaiii, kiwi로 잘라서 List[List[str]] 형태로 받습니다.
4. custom_tokenizer.export_tkd: Tokenized 텍스트를 파일로 출력해둡니다. 워낙 오래 걸리는 작업이기 때문에 tokenizing 후 저장해두도록 합니다.
5. custom_tokenizer.load_tkd: Tokenized된 문장들을 List[List[str]]형태로 불러옵니다. 각 문장이 하나의 List로 받아집니다.
