import random
from datacenter.models import Schoolkid, Mark, Chastisement,\
    Lesson, Commendation, Subject
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


def fix_marks(schoolkid_name):
    """Исправить все плохие оценки (2 и 3) на 5"""
    schoolkid = get_schoolkid(schoolkid_name)
    if schoolkid:
        bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
        bad_marks_count = bad_marks.count()
        bad_marks.update(points=5)
        print(f'Исправлено плохих оценок: {bad_marks_count}')


def remove_chastisements(schoolkid_name):
    """Удалить всю замечания указанного ученика"""
    schoolkid = get_schoolkid(schoolkid_name)
    if schoolkid:
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        chastisements_count = chastisements.count()
        chastisements.delete()
        print(f'Удалено замечаний: {chastisements_count}')


def create_commendation(schoolkid_name, subject_name):
    """Создать похвалу для указанного ученика по указанному предмету"""
    commendations = [
        'Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!'
        'Ты меня приятно удивил!', 'Великолепно!', 'Прекрасно!',
        'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!', 'Очень хороший ответ!',
        'Ты, как всегда, точен!', 'Талантливо!',
        'Ты сегодня прыгнул выше головы!', 'Я поражен!',
        'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!',
        'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!',
        'Здорово!', 'Это как раз то, что нужно!', 'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!',
        'Ты растешь над собой!', 'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!'
    ]
    schoolkid = get_schoolkid(schoolkid_name)
    if schoolkid:
        subject = get_subject(schoolkid, subject_name)
        if subject:
            lessons = Lesson.objects.filter(
                subject=subject,
                year_of_study=schoolkid.year_of_study,
                group_letter=schoolkid.group_letter
            )
            last_lesson = lessons.order_by('-date').first()
            new_commendation = random.choice(commendations)
            Commendation.objects.create(
                text=new_commendation,
                created=last_lesson.date,
                schoolkid=schoolkid,
                subject=subject,
                teacher=last_lesson.teacher
            )
            print(f'Добавлена похвала: "{new_commendation}"')


def get_schoolkid(schoolkid_name):
    """Получить объект ученика по указанному имени"""
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        return schoolkid
    except ObjectDoesNotExist:
        print("Ученик с указанным именем не найден. Проверьте правильность "
              "введенных данных.")
    except MultipleObjectsReturned:
        print("Найдено несколько записей, соответствующих указанному имени. "
              "Требуется более точное указание имени.")


def get_subject(schoolkid, subject_name):
    """Получить объект предмета по объекту ученика и указанному названию"""
    try:
        subject = Subject.objects.get(
            title__contains=subject_name,
            year_of_study=schoolkid.year_of_study
        )
        return subject
    except ObjectDoesNotExist:
        print("Указанный предмет не найден. Проверьте правильность "
              "введенных данных.")
    except MultipleObjectsReturned:
        print("Найдено несколько записей, соответствующих указанному "
              "предмету. Требуется более точное указание предмета.")
