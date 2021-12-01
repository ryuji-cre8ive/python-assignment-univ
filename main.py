#RYUJI KOKUBU
#TP062443

def menu_add():
    loop_add = 'y'
    while loop_add == 'y':
        menu = input('------------\na.Coach\nb.Sport\nc.Sport Schedule\nd.exit\n------------\n')
        if menu == "a":
            add_record()
        if menu == "b":
            add_sport()
        if menu == "c":
            add_schedule()
        if menu == "d":
            loop_add = 'n'


def add_record():
    coach_id = input('What is his/her id?? ').strip()
    coach_name_ = input('What is his/her name?? ').strip()
    joined_date = input('When did his/her participate?? dd/mm ').strip()
    fin_date = input('When will finish?? dd/mm ').strip()
    hourly_rate = input('How much hourly rate?? ').strip()
    tel_num = input('What is his/her telephone number?? ').strip()
    address = input('Where his/her live?? ').strip()
    centre_code = input('What is centre code?? ').strip()
    centre_name = input('What is centre name?? ').strip()
    sport_code = input('What is sport code?? ').strip()
    sport_name = input('What is his/her sport? ').strip()
    c_handle_ = open('coach.txt', "a")
    c_handle_.write(
        f"{coach_id},{coach_name_},{joined_date},{fin_date},{hourly_rate},{tel_num},"
        f"{address},{centre_code},{centre_name},{sport_code},{sport_name},0.0,0.0\n")
    print('this coach is totally accepted!')


def add_sport():
    sport_not_exist = True
    s_handle_read = open('sport.txt', "r")
    s_handle_ = open('sport.txt', "a")

    sport_name = input('Enter new sport ')
    for a in s_handle_read:
        if a.rstrip() == sport_name:
            print('This sport is already exist')
            sport_not_exist = False
            break

    if sport_not_exist:
        s_handle_.write(f"{sport_name}*\n")
        print('totally accepted')
    s_handle_.close()
    s_handle_read.close()


def add_schedule():
    sport_name = input('What is sport name? ')
    sc_handle = open('sport.txt', "r").readlines()
    sc_handle_w = open('sport.txt', "w")
    day_of_week = []
    sport_exist = False
    for b in sc_handle:
        sport_ = b.split('*')
        if sport_[0] == sport_name:
            sport_exist = True
        else:
            sc_handle_w.write(f"{b.strip()}\n")
    if sport_exist:
        loop_sc = "y"
        while loop_sc == "y":
            day_of_week.append(input(f'Enter date of {sport_name} '))
            end_or_succeed = int(input('-------------\n1.succeed\n2.end\n--------------\n'))
            if end_or_succeed == 2:
                loop_sc = "n"
        sc_handle_w.write(f"{sport_name}*{day_of_week}\n")
        sc_handle_w.close()
    else:
        print('Does not exist')


def display_all():
    loop_display = 'y'
    while loop_display == 'y':
        display_menu = int(input('-------------\n1.Coach\n2.Sport\n3.Registered Student\n4.exit\n--------------\n'))
        c_handle__ = open('coach.txt', "r").readlines()
        s_handle__ = open('sport.txt', 'r').readlines()
        stu_handle_ = open('store.txt', "r").readlines()
        if display_menu == 1:
            for c in c_handle__:
                print(c.strip())
        elif display_menu == 2:
            for c in s_handle__:
                print(c.strip())
        elif display_menu == 3:
            for c in stu_handle_:
                if c.split(',')[0].strip() == 'admin':
                    continue
                print(c.split(',')[0].strip())
        elif display_menu == 4:
            loop_display = "n"


def search_record():
    loop_search = 'y'
    while loop_search == 'y':
        menu_search = input('-----------'
                            '\na.Coach by CoachId'
                            '\nb.Coach by overall performance'
                            '\nc.Sport by SportId'
                            '\nd.Student by StudentId'
                            '\ne.Exit'
                            '\n-----------\n')
        if menu_search == "a":
            coach_id = input('What is coach id? ')
            _c_handle = open('coach.txt', 'r').readlines()
            for d in _c_handle:
                if d.split(',')[0].strip() == coach_id.strip():
                    print(d)
        elif menu_search == "b":
            search_num = int(input('What number of value do you want to find? '))
            __c__handle = open('coach.txt', 'r').readlines()
            coach_name_value = []
            for m in __c__handle:
                coach_infor = m.split(',')
                number = str(coach_infor[11])
                num = number.split('.')[0]
                decimal = number.split('.')[1]
                if float(decimal[0]) > 5:
                    num = int(num) + 1
                    decimal = 0
                decimal = str(decimal)
                final_number = float(num) + float(decimal[0]) / 10
                if int(final_number) == search_num:
                    coach_name_value.append(f"{coach_infor[1]}:{int(final_number)}")
            print(coach_name_value)

        elif menu_search == "c":
            _s_handle = open('coach.txt', 'r').readlines()
            sport_id = input('What is soprt id? ')
            sport_is_not_exist = True
            for d in _s_handle:
                if d.split(',')[9].strip() == sport_id.strip():
                    print(d.split(',')[10])
                    sport_is_not_exist = False
                    break

            if sport_is_not_exist:
                print('Does not exist')
        elif menu_search == "d":
            stu_num = input('please enter your finding number').strip()
            __s_handle = open('store.txt', "r").readlines()
            student_name = ""
            is_exist_stu = False
            for q in __s_handle:
                _stu_info = q.split(',')
                if _stu_info[9].strip() == stu_num:
                    student_name = _stu_info[0]
                    is_exist_stu = True
            if is_exist_stu:
                print(student_name)
            else:
                print('You are wrong')
        elif menu_search == 'e':
            loop_search = 'n'
        else:
            print('correct char is only acceptable')


def sort_number(x):
    _c_handle = open('coach.txt', "r").readlines()
    name_list = []
    h = 0
    for e in _c_handle:
        name_list.append(e.split(',')[x])
        h += 1
    o = 0
    if x == 4:
        name_list = list(map(int, name_list))
    if x == 11:
        name_list = list(map(float, name_list))
    while o <= h:
        k = 0
        while k < h - o - 1:
            if name_list[k] > name_list[k + 1]:
                name_list[k], name_list[k + 1] = name_list[k + 1], name_list[k]
            k += 1
        o += 1
    e = 0

    uniqued = []
    count = 0
    for y in name_list:
        if not y in uniqued:
            uniqued.append(y)
            count += 1


    file = open('coach.txt', "w")
    while e < count:
        for c_data in _c_handle:
            if str(uniqued[e]) == c_data.split(",")[x].strip():
                print(c_data.strip())
                file.write(f"{c_data.strip()}\n")
        e += 1
    file.close()


def sort_anything(x):
    _c_handle = open('coach.txt', "r").readlines()
    name_list = []
    h = 0
    for e in _c_handle:
        name_list.append(e.split(',')[x])
        h += 1
    o = 0
    if x == 4 or x == 11:
        name_list = list(map(float, name_list))
    while o <= h:
        k = 0
        while k < h - o - 1:
            if name_list[k] > name_list[k + 1]:
                name_list[k], name_list[k + 1] = name_list[k + 1], name_list[k]
            k += 1
        o += 1
    e = 0
    name_list = list(map(str, name_list))
    file = open('coach.txt', "w")
    while e < h:
        for c_data in _c_handle:
            if name_list[e] == c_data.split(",")[x].strip():
                print(c_data.strip())
                file.write(f"{c_data.strip()}\n")

        e += 1
    file.close()


def sort_and_display():
    loop_sort = 'y'
    while loop_sort == "y":
        menu_sort = input(
            "-------------\na.Coaches in ascending order by names\nb.Coaches Hourly Pay Rate in ascending order"
            "\nc.Coaches Overall Performance in ascending order\nd.Exit\n--------------\n")

        if menu_sort == "a":
            sort_anything(1)

        elif menu_sort == "b":
            sort_number(4)

        elif menu_sort == "c":
            sort_number(11)

        elif menu_sort == "d":
            loop_sort = 'n'


def modify_record():
    loop_modify = 'y'
    while loop_modify == "y":
        modi_menu = input("-------------\na.Coach\nb.Sport\nc.Sport schedule\nd.exit\n-------------\n")
        if modi_menu == "a":
            _c_handle__ = open('coach.txt', "r")
            c_handle_re = _c_handle__.readlines()
            _c_handle__.close()
            _c_handle__ = open('coach.txt', "w")
            coach_id = input("Please fill in coach's Id ").strip()
            _is_exist = False
            coach = ""

            for g in c_handle_re:
                if g.split(',')[0].strip() != coach_id.strip():
                    _c_handle__.write(f"{g.strip()}\n")

                elif g.split(',')[0].strip() == coach_id.strip():
                    _is_exist = True
                    coach = g

            if _is_exist:
                modi_loop = "y"
                coach_array = coach.split(',')
                while modi_loop == "y":
                    modify_num = int(input("-------------\n1.name\n2.date of finish\n3.Hourly rate"
                                           "\n4.Phone number\n5.Address\n6.centre code\n"
                                           "7.centre name\n8.Sport code\n9.Sport name\n10.exit"
                                           "\n-------------\n"))
                    if modify_num == 1:
                        _coach_name = input('Please enter name ')
                        coach_array[1] = _coach_name
                    elif modify_num == 2:
                        coach_finish_date = input("Please enter finish date mm/dd ")
                        coach_array[3] = coach_finish_date
                    elif modify_num == 3:
                        coach_hourly = input("Please enter hourly rate ")
                        coach_array[4] = coach_hourly
                    elif modify_num == 4:
                        coach_phone = input("Please enter Phone number ")
                        coach_array[5] = coach_phone
                    elif modify_num == 5:
                        coach_address = input("Please enter Address ")
                        coach_array[6] = coach_address
                    elif modify_num == 6:
                        coach_centre_code = input("Please enter centre code ")
                        coach_array[7] = coach_centre_code
                    elif modify_num == 7:
                        coach_centre_name = input("Please enter centre name ")
                        coach_array[8] = coach_centre_name
                    elif modify_num == 8:
                        coach_sport_code = input("Please enter sport code ")
                        coach_array[9] = coach_sport_code
                    elif modify_num == 9:
                        coach_sport_name = input("Please enter sport name ")
                        coach_array[10] = coach_sport_name
                    elif modify_num == 10:
                        coach = ",".join(coach_array)
                        _c_handle__.write(f"{coach.strip()}\n")
                        _c_handle__.close()
                        modi_loop = "n"

            else:
                print('is not exist')

        elif modi_menu == "b":
            _s_handle__ = open('sport.txt', "r")
            s_handle_re = _s_handle__.readlines()
            _s_handle__.close()
            _s_handle__ = open('sport.txt', "w")
            sport_name = input("Please fill in sport name ").strip()
            _is_exist = False
            _sport_name = ""

            for g in s_handle_re:
                if g.split('*')[0].strip() != sport_name.strip():
                    _s_handle__.write(f"{g.strip()}\n")

                elif g.split('*')[0].strip() == sport_name.strip():
                    _is_exist = True
                    _sport_name = g
            if _is_exist:
                sport_arr = _sport_name.split('*')
                delete_or_change = input('---------------\na.Change\nb.Delete\n------------------\n')
                if delete_or_change == "a":
                    change_sport = input('please fill in new sport')
                    sport_arr[0] = change_sport
                    _sport_name = "*".join(sport_arr)
                    _s_handle__.write(f"{_sport_name.strip()}\n")
                    _s_handle__.close()

                elif delete_or_change == "b":
                    _s_handle__.close()
                    print('Totally cleared')
            else:
                print('this sport does not exist')

        elif modi_menu == "c":
            sc_handle = open('sport.txt', "r")
            sc_handle_re = sc_handle.readlines()
            sc_handle.close()
            sc_handle = open('sport.txt', "w")
            sport_name = input("Please fill in sport name ").strip()
            _is_exist = False
            _sport_name = ""

            for g in sc_handle_re:
                if g.split('*')[0].strip() != sport_name.strip():
                    sc_handle.write(f"{g.strip()}\n")

                elif g.split('*')[0].strip() == sport_name.strip():
                    _is_exist = True
                    _sport_name = g
            print(_sport_name)
            if _is_exist:
                sport_arr = _sport_name.split('*')
                delete_or_change = input('---------------\na.Change\nb.Delete\n------------------\n')
                if delete_or_change == "a":
                    day_of_week = []
                    loop_sport = "y"
                    while loop_sport == "y":
                        day_of_week.append(input(f'Enter date of {sport_name} '))
                        end_or_suceed = int(input('-------------\n1.succeed\n2.end\n--------------\n'))
                        if end_or_suceed == 2:
                            loop_sport = "n"

                    sc_handle.write(f"{sport_arr[0]}*{day_of_week},\n")
                    sc_handle.close()
                    print('Totally accepted!')

                elif delete_or_change == "b":
                    sc_handle.write(f"{sport_arr[0]},\n")
                    sc_handle.close()
                    print('Totally accepted!')
            else:
                print('this sport does not exist')
        elif modi_menu == "d":
            loop_modify = "n"
        else:
            print('try again')


def exit_user():
    print('see you next time!')


loop_first = "y"
print('****************\nWelcome to RCSAS!\n***************')
while loop_first == "y":

    main_menu = int(input('------------\n1.login\n2.View Sport\n3.View Sports Schedule\n4.Register\n--------------\n'))
    if main_menu == 3:
        s_handle = open('sport.txt', 'r').readlines()
        j = 0
        for i in s_handle:
            if not i.strip().split('*')[1]:
                continue
            else:
                print(i.strip())
                j += 1
        if j == 0:
            print('Schedule is not registered')
    elif main_menu == 2:
        s_handle = open('sport.txt', 'r').readlines()
        for i in s_handle:
            print(i.split('*')[0])
    elif main_menu == 4:
        newer_name = input('Please fill in your name ')
        newer_password = input('Please fill in your password ')
        stu_handle = open('store.txt', "r")
        is_registered = False
        count = 0
        for i in stu_handle:
            name = i.split(',')[0]
            if newer_name == name:
                is_registered = True
            count = count + 1
        stu_handle.close()
        if is_registered:
            print('You are already registered')
        else:
            stu_handle_w = open('store.txt', "a")
            stu_handle_w.write(f"{newer_name},{newer_password},name,sex,old,address,e-mail,"
                               f"phone_number,sport,{count}\n")
            stu_handle_w.close()
            print('You are totally accepted')

    elif main_menu == 1:
        user_name = input('Enter your name: ')
        password = input('Enter your password: ')
        loop = 'y'

        is_admin = False
        is_user = False
        f = open('store.txt', "r")
        for i in f:

            stored_name = i.strip().split(',')[0]
            stored_password = i.strip().split(',')[1]

            if user_name == stored_name and password == stored_password and user_name == 'admin':
                is_admin = True
                break
            elif user_name == stored_name and password == stored_password:
                is_user = True
                break

        if is_admin:
            print('****************\nWelcome to admin!\n***************')
            print('Please select your menu\n')
            while loop == 'y':
                menu_main = int(input(
                    '---------------\n1.Add Records\n2.Display All Records\n'
                    '3.Search specific records\n4.Sort and Display '
                    'records\n5.Modify records\n6.Exit\n---------------\n'))
                if menu_main == 1:
                    menu_add()

                elif menu_main == 2:
                    display_all()

                elif menu_main == 3:
                    search_record()

                elif menu_main == 4:
                    sort_and_display()

                elif menu_main == 5:
                    modify_record()

                elif menu_main == 6:
                    exit_user()
                    loop = 'n'
                    loop_first = "n"
                else:
                    print('please enter correct number')

        elif is_user:
            loop_user = 'y'
            print(f'Hello, {user_name}!')
            while loop_user == 'y':
                user_menu = int(input(
                    '--------------------\n1.View Details\n2.Modify Self Record'
                    '\n3.FeedBack to Coach\n4.Exit\n--------------------\n'))
                if user_menu == 1:
                    details_loop = 'y'
                    while details_loop == 'y':
                        details_menu = input(
                            '--------------\na.Coach\nb.Self-Record\nc.Registered Sport\nd.Exit\n-------------\n')
                        if details_menu == 'a':
                            c_handle = open('coach.txt', "r").readlines()
                            for i in c_handle:
                                coach_info = i.split(',')
                                print(
                                    f"name:{coach_info[1]} Handling_sport:{coach_info[10]} "
                                    f"Star:{coach_info[11]} fee/hour:{coach_info[4]} "
                                    f"phone_number:{coach_info[5]} Sport_sentre:{coach_info[8]}")
                        elif details_menu == 'b':
                            stu_handle = open('store.txt', "r").readlines()

                            for i in stu_handle:
                                stu_info = i.split(',')
                                if stu_info[0] == user_name:
                                    if stu_info[3] == "sex":
                                        print('Your information is still not registered.')
                                    else:
                                        print(f"name:{stu_info[2]}\nsex:{stu_info[3]}\n"
                                              f"old:{stu_info[4]}\naddress:{stu_info[5]}\ne-mail:{stu_info[6]}"
                                              f"\nphone_number:{stu_info[7]}\nsport:{stu_info[8]}")

                        elif details_menu == 'c':
                            stu_handle = open('store.txt', "r").readlines()
                            s_handle = open('sport.txt', 'r').readlines()
                            stu_sport = ""
                            is_not_registered = False
                            for i in stu_handle:
                                stu_info = i.split(',')

                                if stu_info[0] == user_name:

                                    for j in s_handle:
                                        sport = j.split('*')
                                        if sport[0].strip() == stu_info[8].strip():
                                            if sport[1].strip() == "":
                                                print(f"{sport[0]}'s schedule still not registered")
                                            else:
                                                print(f"{sport[0]}:{sport[1]}")
                                        elif stu_info[8].strip() == "sport":
                                            is_not_registered = True
                                    if is_not_registered:
                                        print('You must modify your sports first')
                        elif details_menu == 'd':
                            details_loop = 'n'
                            print('see you!')

                elif user_menu == 2:
                    print('Now, you can add your personal information')
                    name = input('What is your name? ')
                    user_sex = input('What is your sex? ')
                    user_old = input('How old are you? ')
                    user_address = input('Where do you live? ')
                    user_mail = input('What is your e-mail? ')
                    user_phone = input('What is your phone number? ')
                    user_sport = input('What is your sport? ')

                    stu_handle_r = open('store.txt', "r").readlines()
                    stu_handle = open('store.txt', "w")
                    is_exist = False

                    user = ""
                    for i in stu_handle_r:
                        stu_info = i.split(",")
                        if stu_info[0] == user_name:
                            is_exist = True
                            user = i
                        else:
                            stu_handle.write(f"{i}")
                    if is_exist:
                        user_id = user.split(",")[9]
                        stu_handle.write(f"{user_name},{password},{name},{user_sex},{user_old},"
                                         f"{user_address},{user_mail},{user_phone},{user_sport},{user_id}\n")
                        stu_handle.close()

                        print('You are totally accepted!')

                elif user_menu == 3:
                    c_handle = open('coach.txt', 'r').readlines()
                    coach_name = input('Which coach do you want to review? ')
                    coach_exist = False
                    c_handle_w = open('coach.txt', 'w')

                    specify_coach = ''
                    for i in c_handle:
                        coach_info = i.split(',')
                        if coach_name == coach_info[1]:
                            coach_exist = True
                            specify_coach = i
                        else:
                            c_handle_w.write(f"{i.strip()}\n")
                    if coach_exist:
                        loop_review = 'y'
                        review = 0
                        while loop_review == "y":
                            review = int(input("What is coach's score? 1~5"))
                            if review > 6 or review < 0:
                                print('Please enter right number!')
                            loop_review = 'n'
                        coach_arr = specify_coach.split(',')
                        old_review = float(coach_arr[11])
                        how_many = int(coach_arr[12])
                        need_info = ','.join(coach_arr[0:11])

                        new_review = (old_review * how_many + review) / (how_many + 1)
                        new_review = str(new_review)
                        decimal = new_review.split('.')[1]
                        number = new_review.split('.')[0]
                        decimal = float(decimal)
                        number = float(number)
                        if int(decimal) >= 5:
                            number = number + 1
                            decimal = 0
                        final_review = number + decimal / 10
                        print(f'{coach_arr[1]}:{final_review}')

                        c_handle_w.write(f"{need_info},{float(final_review)},{int(how_many) + 1}")
                        print('You are totally accepted!')
                    else:
                        print('This coach does not exists')
                    c_handle_w.close()
                elif user_menu == 4:
                    loop_user = 'n'
                    print("See you again!")
                else:
                    print('error')
            loop_first = "n"
        else:
            print('u r not registerd')
