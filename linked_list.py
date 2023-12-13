import heapq

"""
1. Об’єднати два відсортовані списки
Вам надано заголовки двох відсортованих пов’язаних списків list1 і list2.

Об’єднайте два списки в один відсортований список. Список має бути створений шляхом з’єднання вузлів перших
двох списків.

Повернути заголовок об’єднаного зв’язаного списку.

Приклад 1:
Node1 (1) --> Node1 (2) --> Node1 (4)
Node2 (1) --> Node2 (3) --> Node2 (4)
Node1 (1) --> Node2 (1) --> Node1 (2) --> Node2 (3) --> Node1 (4) --> Node2 (4)
Input: list1 = [ 1, 2, 4 ], list2 = [ 1, 3, 4 ]
Output: [ 1, 1, 2, 3, 4, 4 ]

Приклад 2:
Input: list1 = [ ], list2 = [ ]
Output: [ ]

Приклад 3:
Input: list1 = [ ], list2 = [ 0 ]
Output: [ 0 ]

Обмеження:
Кількість вузлів в обох списках знаходиться в діапазоні [ 0, 50 ].
-100 <= Node.val <= 100
Обидва list1 і list2 відсортовані за неспаданням.
"""


class LinkedList1:
    def __init__(self, val=0, next=None):
        if not (-100 <= val <= 100):
            raise ValueError('val must be in range [-100, 100]')
        self.val = val
        self.next = next


def merge_sorted_lists(list1, list2):
    if 0 >= len(list1) > 50 or 0 >= len(list2) > 50:

        dummy = LinkedList1()  # вузол-заглушка для початку нового списку
        current = dummy  # поточний вузол, щоб рухатися по новому списку

        while list1 is not None and list2 is not None:
            # порівнюємо значення вузлів і додаємо менше значення до нового списку
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # додаємо залишок, якщо один зі списків закінчився
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2

        # повертаємо початок об'єднаного списку (поза заглушкою)
        return dummy.next
    else:
        raise ValueError('Node values must be in range [0, 50]')


def print_list(node):
    # Функція виводу списку вузлів
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


def check_sorted_list(list1_input, list2_input):
    # перевірка, чи списки відсортовані за неспаданням
    if list1_input != sorted(list1_input, reverse=True):
        raise ValueError("list1 is not sorted in non-decreasing order")

    if list2_input != sorted(list2_input, reverse=True):
        raise ValueError("list2 is not sorted in non-decreasing order")

    # Запускаємо алгоритм перевірки
    if list1_input:
        list1 = LinkedList1(list1_input[0])
        current = list1
        for val in list1_input[1:]:
            current.next = LinkedList1(val)
            current = current.next
    else:
        list1 = None

    if list2_input:
        list2 = LinkedList1(list2_input[0])
        current = list2
        for val in list2_input[1:]:
            current.next = LinkedList1(val)
            current = current.next
    else:
        list2 = None

    # Об'єднання списків
    result = merge_sorted_lists(list1, list2)

    return print_list(result)


# Тестуємо:
# list1 = [1, 2, 4]
# list2 = [1, 3, 4]
# print(check_sorted_list(list1, list2))
#
# list3 = []
# list4 = []
# print(check_sorted_list(list3, list4))
#
# list5 = []
# list6 = [0]
# print(check_sorted_list(list5, list6))

# ______________________________________________________________________________________________________________________

"""
2. Видалити дублікати з відсортованого списку
Враховуючи head відсортованого пов’язаного списку, видаліть усі дублікати, щоб кожен елемент з’являвся лише один раз. 
Поверніть зв’язаний список також відсортованим.

Приклад 1:
Input: head = [ 1, 1, 2 ] 
Output: [ 1, 2 ]

Приклад 2:
Input: head = [ 1, 1, 2, 3, 3 ] 
Output: [ 1, 2, 3 ]

Обмеження:
Кількість вузлів у списку знаходиться в діапазоні [0, 300].
-100 <= Node.val <= 100
Список гарантовано буде відсортований у порядку зростання.
"""


class LinkedList2:
    def __init__(self, val=0, next=None):
        if not (-100 <= val <= 100):
            raise ValueError('val must be in range [-100, 100]')
        self.val = val
        self.next = next


def delete_duplicates(head):
    # Функція видалення дублікатів з відсортованого зв'язаного списку.
    current = head

    while current is not None and current.next is not None:
        if current.val == current.next.val:
            # Видаляємо дублікат, якщо вони існують
            current.next = current.next.next
        else:
            # Переходимо до наступного елементу
            current = current.next

    return head


def print_list(node):
    # Функція перетворення зв'язаний список в список значень.
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


def check_delete_duplicates(head_values):
    # Перевіряємо та видаляємо дублікати зі вхідного списку.
    if not 0 <= len(head_values) <= 300:
        raise ValueError("The number of nodes should be in the range [0, 300]")

    # Перевірка, чи список відсортований у порядку зростання
    if head_values != sorted(head_values):
        raise ValueError("The list is not sorted in non-decreasing order")

    # Запускаємо алгоритм перевірки та видалення дублікатів
    if head_values:
        head = LinkedList2(head_values[0])
        current = head
        for val in head_values[1:]:
            current.next = LinkedList2(val)
            current = current.next
    else:
        head = None

    result = delete_duplicates(head)

    return print_list(result)


# Тестуємо:
# head1 = [1, 1, 2]
# head2 = [1, 1, 2, 3, 3]
#
# print(check_delete_duplicates(head1))
# print(check_delete_duplicates(head2))

# ______________________________________________________________________________________________________________________

"""
3. Цикл пов’язаного списку
Дана head, голова зв’язаного списку, визначає, чи містить зв’язаний список цикл.

У зв’язаному списку існує цикл, якщо в списку є якийсь вузол, до якого можна знову повернутися, постійно переходячи за 
next вказівником. Внутрішньо pos використовується для позначення індексу вузла, до якого підключено next покажчик 
хвоста. Зауважте, що pos не передається як параметр.

Повертає true, якщо у пов’язаному списку є цикл. В іншому випадку поверніть false.

Приклад 1:
Input: head = [ 3, 2, 0, -4 ], pos = 1 Output: true Пояснення: У пов’язаному списку є цикл, де хвіст з’єднується 
з 1-м вузлом (з індексом 0).

Приклад 2:
Input: head = [ 1, 2 ], pos = 0 
Output: true 
Пояснення: У пов’язаному списку є цикл, де хвіст з’єднується з 0-м вузлом.

Приклад 3:
Input: head = [ 1 ], pos = -1 
Output: false Пояснення: У пов’язаному списку немає жодного циклу.

Обмеження:
Кількість вузлів у списку знаходиться в діапазоні [0, 10 000].
-100 000 <= Node.val <= 100 000
pos це -1 чи дійсний індекс у пов’язаному списку.
"""


class LinkedList3:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    # Перевіряє наявність циклу у зв'язаному списку.
    if not head:
        return False  # Немає циклу, якщо список порожній

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next  # Повільний рухається зі швидкістю 1
        fast = fast.next.next  # Швидкий рухається зі швидкістю 2

        if slow == fast:
            return True  # Знайдено цикл

    return False  # Немає циклу


def create_linked_list_with_cycle(values, pos):
    # Створює зв'язаний список із циклом за заданими значеннями та позицією циклу.
    if not (0 <= len(values) <= 10000):
        raise ValueError("The number of nodes should be in the range [0, 10,000]")

    if any(not (-100000 <= val <= 100000) for val in values):
        raise ValueError("Node values should be in the range [-100,000, 100,000]")

    if not (-1 <= pos < len(values)):
        raise ValueError("pos should be -1 or a valid index in the linked list")

    if not values:
        return None

    head = LinkedList3(values[0])
    current = head

    for val in values[1:]:
        current.next = LinkedList3(val)
        current = current.next

    if pos != -1:
        # Знайдемо вузол, до якого підключений хвіст для утворення циклу
        cycle_node = head
        for i in range(pos):
            cycle_node = cycle_node.next

        current.next = cycle_node

    return head


# Тестуємо:
# head1_values = [3, 2, 0, -4]
# pos1 = 1
# linked_list1 = create_linked_list_with_cycle(head1_values, pos1)
# print(has_cycle(linked_list1))
#
# head2_values = [1, 2]
# pos2 = 0
# linked_list2 = create_linked_list_with_cycle(head2_values, pos2)
# print(has_cycle(linked_list2))
#
# head3_values = [1]
# pos3 = -1
# linked_list3 = create_linked_list_with_cycle(head3_values, pos3)
# print(has_cycle(linked_list3))

# ______________________________________________________________________________________________________________________

"""
4. Перевпорядкувати список
Вам надається head однозв’язаного списку. Список можна представити у вигляді:

L0 → L1 → … → Ln - 1 → Ln

Перевпорядкуйте список у такій формі:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

Ви не можете змінювати значення у вузлах списку. Змінювати можна лише самі вузли.

Приклад 1:
Input: head = [ 1, 2, 3, 4 ] Output: [ 1, 4, 2, 3 ]

Приклад 2:
Input: head = [ 1, 2, 3, 4, 5 ] Output: [ 1, 5, 2, 4, 3 ]

Обмеження:
Кількість вузлів у списку знаходиться в діапазоні [ 1, 5 * 10 000].
1 <= Node.val <= 1 000
"""


class LinkedList4:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head):
    # Функція перевпорядковує заданий однозв'язаний список у вказаному порядку.

    if not head or not head.next:
        return head

    # Знайдемо середину списку
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Розділити список на дві частини
    second_half = slow.next
    slow.next = None

    # Обернути другу половину
    prev = None
    current = second_half

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    # З'єднати обидві частини списку
    first_half = head
    second_half = prev

    while second_half:
        temp1 = first_half.next
        temp2 = second_half.next

        first_half.next = second_half
        second_half.next = temp1

        first_half = temp1
        second_half = temp2

    return head


def print_list(node):
    # Функція виводить значення вузлів списку.
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def create_linked_list(values):
    # Функція створює однозв'язаний список із заданими значеннями.
    if not (0 < len(values) <= 50000):
        raise ValueError("The number of nodes should be in the range [1, 50000]")

    if any(not (1 <= val <= 1000) for val in values):
        raise ValueError("Node values should be in the range [1, 1000]")

    head = LinkedList4(values[0])
    current = head

    for val in values[1:]:
        current.next = LinkedList4(val)
        current = current.next

    return head


def check_list(values):
    # Запускаємо алгоритм перевірки
    linked_list = create_linked_list(values)
    reorder_list(linked_list)
    return print_list(linked_list)


# Тестуємо:
# values1 = [1, 2, 3, 4]
# values2 = [1, 2, 3, 4, 5]
# print(check_list(values1))
# print(check_list(values2))

# ______________________________________________________________________________________________________________________

"""
5. Видалити вузол у зв’язаному списку
Існує head списку з одним зв’язком, і ми хочемо видалити вузол node в ньому.

Вам надається node, який потрібно видалити. Вам не буде надано доступ до першого вузла head.

Усі значення пов’язаного списку є унікальними, і гарантується, що заданий вузол node не є останнім вузлом у зв’язаному 
списку.

Видалити вказаний вузол. Зауважте, що видаляючи вузол, ми не маємо на увазі видалення його з пам’яті. Ми маємо на увазі:
Значення даного вузла не повинно існувати у зв’язаному списку.
Кількість вузлів у пов’язаному списку має зменшитися на один.
Усі значення перед node мають бути в однаковому порядку.
Усі значення після node мають бути в однаковому порядку.
Спеціальне тестування:
Для введення ви повинні надати повну head пов’язаного списку та вузол, якому буде надано node. node не повинен бути 
останнім вузлом списку, а повинен бути фактичним вузлом у списку.
Ми створимо пов’язаний список і передамо вузол вашій функції.
Результатом буде весь список після виклику вашої функції.

Приклад 1:
Input: head = [ 4, 5, 1, 9 ], node = 5 
Output: [ 4, 1, 9 ] 
Пояснення: Вам надається другий вузол зі значенням 5, зв’язаний список має стати 4 -> 1 -> 9 після виклику вашої функції

Приклад 2:
Input: head = [ 4, 5, 1, 9 ], node = 1 
Output: [ 4, 5, 9 ]

Обмеження:
Кількість вузлів у наданому списку знаходиться в діапазоні [2, 1000].
-1000 <= Node.val <= 1000
Значення кожного вузла в списку є унікальним.
node, який потрібно видалити, є у списку і не є хвостовим вузлом.
"""


class LinkedList5:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_node(node):
    # Функція видаляє заданий вузол зі зв'язаного списку.
    node.val = node.next.val
    node.next = node.next.next


def create_linked_list(values):
    # Функція cтворює зв'язаний список із заданими значеннями.
    if not (2 <= len(values) <= 1000):
        raise ValueError("The number of nodes should be in the range [2, 1000]")

    if any(not (-1000 <= val <= 1000) for val in values):
        raise ValueError("Node values should be in the range [-1000, 1000]")

    # Перевірка унікальності значень вузлів
    if len(values) != len(set(values)):
        raise ValueError("Node values should be unique")

    head = LinkedList5(values[0])
    current = head

    for val in values[1:]:
        current.next = LinkedList5(val)
        current = current.next

    return head


def print_list(node):
    # Функція виводить значення вузлів списку.
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def check_delete_node(head_values, node_to_delete_value):
    # Запускаємо алгоритм перевірки
    head_node = create_linked_list(head_values)
    node_to_delete = head_node

    while node_to_delete and node_to_delete.val != node_to_delete_value:
        node_to_delete = node_to_delete.next

    # Перевірка, чи знайдено вузол для видалення
    if not node_to_delete or not node_to_delete.next:
        raise ValueError("Invalid node to delete")

    delete_node(node_to_delete)
    return print_list(head_node)


# Тестуємо:
# head1 = [4, 5, 1, 9]
# node1 = 5
# head2 = [4, 5, 1, 9]
# node2 = 1
# print(check_delete_node(head1, node1))
# print(check_delete_node(head2, node2))

# ______________________________________________________________________________________________________________________

"""
6. Подвоїти число, представлене у вигляді зв’язаного списку
Вам надано head непорожнього зв’язаного списку, що представляє невід’ємне ціле число без нулів на початку.

Повернути head пов’язаного списку після її подвоєння.

Приклад 1:
Input: head = [ 1,8, 9 ] 
Output: [ 3, 7, 8 ] 
Пояснення: Число вище відповідає даному зв’язаному списку, який представляє число 189. Отже, повернутий зв’язаний 
список представляє число 189 * 2 = 378

Приклад 2:
Input: head = [ 9, 9, 9 ] 
Output: [ 1, 9, 9, 8 ]

Обмеження:
Кількість вузлів у списку знаходиться в діапазоні [1, 10 000]
0 <= Node.val <= 9
Вхідні дані створюються таким чином, що список представляє число, яке не має початкових нулів, окрім самого числа 0.
"""


class LinkedList6:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def double_linked_list(head):
    # Перетворюємо зв'язаний список в число
    num = 0
    current = head
    while current:
        num = num * 10 + current.val
        current = current.next

    # Подвоюємо число
    num *= 2

    # Розбиваємо число на окремі цифри і створюємо новий зв'язаний список
    dummy = LinkedList6()
    current = dummy

    for digit in str(num):
        current.next = LinkedList6(int(digit))
        current = current.next

    return dummy.next


def create_linked_list6(values):
    if not (1 <= len(values) <= 10000):
        raise ValueError("The number of nodes should be in the range [1, 10000]")

    if any(not (0 <= val <= 9) for val in values):
        raise ValueError("Node values should be in the range [0, 9]")

    # Перевірка, щоб упевнитися, що число не має початкових нулів, окрім самого числа 0
    if len(values) > 1 and values[0] == 0:
        raise ValueError("The list should represent a number without leading zeros, except for the number 0")

    head = LinkedList6(values[0])
    current = head

    for val in values[1:]:
        current.next = LinkedList6(val)
        current = current.next

    return head


def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def check_double_list(value):
    linked_list = create_linked_list6(value)
    result = double_linked_list(linked_list)
    return print_list(result)


# Тестуємо:
# head1 = [1, 8, 9]
# head2 = [9, 9, 9]
# print(check_double_list(head1))
# print(check_double_list(head2))

# ______________________________________________________________________________________________________________________

"""
7. Об’єднати k відсортованих списків
Вам надано масив із k зв’язаних списків lists, кожен зв’язаний список відсортований у порядку зростання.

Об’єднайте всі зв’язані списки в один відсортований зв’язаний список і поверніть його.

Приклад 1:
Input: lists = [ [ 1, 4, 5 ], [ 1, 3, 4 ], [ 2, 6 ] ] 
Output: [ 1, 1, 2, 3, 4, 4, 5, 6 ] 
Пояснення: Зв’язані списки це: 
[ 
 1 -> 4 -> 5, 
 1 -> 3 -> 4, 
 2 -> 6 ] 
об’єднавши їх в один відсортований список: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

Приклад 2:
Input: lists = [ ] 
Output: [ ]

Приклад 3:
Input: lists = [ [ ] ] 
Output: [ ]

Обмеження:
k == lists.length
0 <= k <= 10 000
0 <= lists[ i ].length <= 500
-104 <= lists[ i ][ j ] <= 10 000
lists[ i ] відсортований в зростаючому порядку.
Сума lists[ i ].length не перевищуватиме 10 000
"""


class LinkedList7:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_sorted_lists(lists):
    # Об'єднуємо k відсортованих списків в один відсортований зв'язаний список.

    # Перевірка обмежень
    k = len(lists)
    if not (0 <= k <= 10_000):
        raise ValueError("k should be in the range [0, 10,000]")

    total_nodes = sum(len(lst) for lst in lists)
    if not (0 <= total_nodes <= 10_000):
        raise ValueError("The total number of nodes should be in the range [0, 10,000]")

    for i, lst in enumerate(lists):
        if not (0 <= len(lst) <= 500):
            raise ValueError("The number of nodes in each list should be in the range [0, 500]")

        if i < k - 1 and not all(lst[j] <= lst[j + 1] for j in range(len(lst) - 1)):
            raise ValueError("Each list should be sorted in ascending order")

        for val in lst:
            if not (-10_000 <= val <= 10_000):
                raise ValueError("Node values should be in the range [-10,000, 10,000]")

    min_heap = []

    # Додаємо перший вузол кожного списку до min-heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    dummy = LinkedList7()
    current = dummy

    while min_heap:
        val, i, idx = heapq.heappop(min_heap)

        # Додаємо поточний вузол до списку
        current.next = LinkedList7(val)
        current = current.next

        # Перевіряємо, чи є наступний вузол у вибраному списку
        if idx + 1 < len(lists[i]):
            heapq.heappush(min_heap, (lists[i][idx + 1], i, idx + 1))

    return dummy.next


def create_linked_list(values):
    # Створюємо зв'язаний список з заданих значень

    if not (0 <= len(values) <= 500):
        raise ValueError("The number of nodes should be in the range [0, 500]")

    if not values:
        return None

    head = LinkedList7(values[0])
    current = head

    for val in values[1:]:
        current.next = LinkedList7(val)
        current = current.next

    return head


def print_list7(node):
    # Повертаємо значення вузлів зв'язаного списку у вигляді списку

    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def check_merge(lists):
    # Запускаємо алгоритм перевірки
    result = merge_k_sorted_lists(lists)
    return print_list(result)


# Тестуємо:
# lists1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
# lists2 = []
# lists3 = [[]]
# print(check_merge(lists1))
# print(check_merge(lists2))
# print(check_merge(lists3))

# ______________________________________________________________________________________________________________________

"""
8. Розвернути вузли в k-групі
Враховуючи head зв’язаного списку, перевертайте вузли списку k за раз і повертайте змінений список.

k є додатним цілим числом і менше або дорівнює довжині пов’язаного списку. Якщо кількість вузлів не кратна k, 
то пропущені вузли, зрештою, повинні залишитися такими, як є.

Ви не можете змінювати значення у вузлах списку, можна змінювати лише самі вузли.

Приклад 1:
Input: head = [ 1, 2, 3, 4, 5 ], k = 2 
Output: [ 2, 1, 4, 3, 5 ]

Приклад 2:
Input: head = [ 1, 2, 3, 4, 5 ], k = 3 
Output: [ 3, 2, 1, 4, 5 ]

Обмеження:
Кількість вузлів у списку дорівнює n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
"""


class LinkedList8:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k):
    # Перевертаємо вузли в групах по k в зв'язаному списку.

    def reverse_group(start, end):
        # Перевертаємо групу вузлів між start і end.

        prev, current = None, start
        while current != end:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    def get_length(node):
        # Отримуємо довжину зв'язаного списку.

        length = 0
        while node:
            length += 1
            node = node.next
        return length

    n = get_length(head)

    if not (1 <= n <= 5000):
        raise ValueError("Кількість вузлів у списку повинна бути в діапазоні [1, 5000]")

        # Перевірка на валідність k
    if not (1 <= k <= n):
        raise ValueError("k повинно бути в діапазоні [1, n]")

    # Створюємо фіктивний вузол для спрощення коду
    dummy = LinkedList8(0)
    dummy.next = head

    prev, curr_group_start = dummy, head

    # Перевертаємо групи вузлів по k
    while n >= k:
        curr_group_end = curr_group_start
        for _ in range(k):
            curr_group_end = curr_group_end.next

        prev.next = reverse_group(curr_group_start, curr_group_end)

        curr_group_start.next = curr_group_end

        prev = curr_group_start
        curr_group_start = curr_group_start.next
        n -= k

    return dummy.next


def create_linked_list8(values):
    # Створюємо зв'язаний список із заданих значень.

    if not (0 <= len(values) <= 5000):
        raise ValueError("Кількість вузлів повинна бути в діапазоні [0, 5000]")

    if not values:
        return None

    head = LinkedList8(values[0])
    current = head

    for val in values[1:]:
        current.next = LinkedList8(val)
        current = current.next

    return head


def print_list8(node):
    # Перетворюємо зв'язаний список в список для виведення.

    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def check_reverse(head, k):
    # Запускаємо алгоритм перевірки
    head = create_linked_list8(head)
    output = reverse_k_group(head, k)
    return print_list8(output)


# Тестуємо:
# head1 = [1, 2, 3, 4, 5]
# k1 = 2
#
# head2 = [1, 2, 3, 4, 5]
# k2 = 3
#
# print(check_reverse(head1, k1))
# print(check_reverse(head2, k2))

# ______________________________________________________________________________________________________________________

"""
9. Розділити список
Маючи head зв’язаного списку та значення x, розділіть його так, щоб усі вузли, менші за x, стояли перед вузлами, 
більшими або рівними x.

Ви повинні зберегти вихідний відносний порядок вузлів у кожній із двох секцій.

Приклад 1:
Input: head = [ 1, 4, 3, 2, 5, 2 ], x = 3 
Output: [ 1, 2, 2, 4, 3, 5 ]

Приклад 2:
Input: head = [ 2, 1 ], x = 2 
Output: [ 1, 2 ]

Обмеження:
Кількість вузлів у списку знаходиться в діапазоні [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""


class LinkedList9:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head, x):
    # Розділяємо зв'язаний список так, щоб вузли менші за x стояли перед вузлами, більшими або рівними x.

    if not (-200 <= x <= 200):
        raise ValueError("The value of x should be in the range [-200, 200]")

    smaller_head = LinkedList9()
    smaller_current = smaller_head

    greater_head = LinkedList9()
    greater_current = greater_head

    current = head

    # Розділяємо вузли
    while current:
        if current.val < x:
            smaller_current.next = current
            smaller_current = smaller_current.next
        else:
            greater_current.next = current
            greater_current = greater_current.next

        current = current.next

    # З'єднуємо два списки
    smaller_current.next = greater_head.next
    greater_current.next = None

    return smaller_head.next


def create_linked_list9(values):
    # Створюємо зв'язаний список із заданих значень.

    if not (0 <= len(values) <= 200):
        raise ValueError("The number of nodes should be in the range [0, 200]")

    if not all(-100 <= val <= 100 for val in values):
        raise ValueError("Node values should be in the range [-100, 100]")

    if not values:
        return None

    head = LinkedList9(values[0])
    current = head

    for val in values[1:]:
        current.next = LinkedList9(val)
        current = current.next

    return head


def print_list9(node):
    # Перетворюємо зв'язаний список в список для виведення.

    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def check_partition(head, x):
    # Запускаємо алгоритм перевірки
    head = create_linked_list9(head)
    output = partition(head, x)
    return print_list9(output)


# Тестуємо:
# head1 = [1, 4, 3, 2, 5, 2]
# x1 = 3
#
# head2 = [2, 1]
# x2 = 2
#
# print(check_partition(head1, x1))
# print(check_partition(head2, x2))
