# -*- coding: utf-8 -*-
'''
履歴機能を実装する前の質問テーブルの回答を回答テーブルに移行
'''

import os, django, sys

sys.path.append('/Users/oshibajunki/mydjango/esuits_junki/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()
from esuits.models import QuestionModel as qm, AnswerModel as am


all_answer_question_record = list(am.objects.all().values_list('question', flat=True))
print(all_answer_question_record)
all_questions_record = qm.objects.all().order_by('pk')
for q in all_questions_record:
    if q.pk not in all_answer_question_record:
        am.objects.create(
            question=q,
            version=1,
            answer=q.answer
            )
