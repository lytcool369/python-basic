# 문제2. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.

import re

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
            To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

## 풀이1.
result = []
for line in s.split('\n'):
    word_result = []
    for word in line.split('<'):
        if word.find('>') == -1:
            word_result.append(word)
        elif word.find('>') != len(word) -1:
            word_result.append(word[word.find('>') + 1:])
    result.append(' '.join(word_result))
print('\n'.join(result))


## 풀이2.
