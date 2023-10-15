class Stack:
    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items

    def is_empty(self):
        return len(self.__items) == 0

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__items.pop()

    def __str__(self):
        return ', '.join(map(str, self.__items))


class TaskManager:
    def __init__(self):
        self.__stack = Stack()

    def new_task(self, task, priority):
        item = (task, priority)
        if item not in self.__stack.items:
            self.__stack.push(item)

    def remove_task(self, task):
        temp_stack = Stack()
        removed = False

        while not self.__stack.is_empty():
            item = self.__stack.pop()
            if item[0] != task:
                temp_stack.push(item)
            else:
                removed = True

        while not temp_stack.is_empty():
            self.__stack.push(temp_stack.pop())

        if not removed:
            print('Такой задачи нет')

    def __str__(self):
        temp_stack = Stack()
        tasks_dict = {}
        ordered = []

        for tsk in self.__stack.items:
            if tsk[1] not in tasks_dict:
                tasks_dict[tsk[1]] = []
            tasks_dict[tsk[1]].append(tsk[0])

        sorted_priorities = sorted(tasks_dict.keys())

        for priority in sorted_priorities:
            tasks = tasks_dict[priority]
            ordered.append(f"{priority} {', '.join(tasks)}")

        while not temp_stack.is_empty():
            self.__stack.push(temp_stack.pop())

        print('\nРезультат: ')
        return '\n'.join(ordered)


def print_result():
    manager = TaskManager()
    manager.new_task('Помыть посуду', 2)
    # добавляем дубликат
    manager.new_task('Помыть посуду', 2)
    manager.new_task('Заправить машину', 4)
    manager.new_task('Сделать уборку', 3)
    manager.new_task('Приготовить ужин', 3)
    manager.new_task('Выгулять собаку', 1)
    manager.new_task('Посмотреть сериал', 5)

    print(manager)

    manager.remove_task('Отдохнуть')
    manager.remove_task('Помыть посуду')

    print(manager)
