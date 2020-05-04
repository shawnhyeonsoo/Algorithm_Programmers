def change(melody):
    if 'A#' in melody: melody = melody.replace('A#', 'a')
    if 'C#' in melody: melody = melody.replace('C#', 'c')
    if 'D#' in melody: melody = melody.replace('D#', 'd')
    if 'F#' in melody: melody = melody.replace('F#', 'f')
    if 'G#' in melody: melody = melody.replace('G#', 'g')
    return melody

def solution(m,musicinfos):
    m = change(m)
    answer = ('(None)', None)
    for i in musicinfos:
        test = list(i.split(','))
        start_hr = int(test[0][:2])
        start_min = int(test[0][3:])
        end_hr = int(test[1][:2])
        end_min = int(test[1][3:])


        duration = ((end_hr*60)+end_min) - ((start_hr*60)+start_min)

        notes = change(test[-1])

        melody = notes*(duration//len(notes))+notes[:duration%len(notes)]

        if m in melody:
            if (answer[1] == None) or (duration > answer[1]):
                answer = (test[2], duration)

    return answer[0]