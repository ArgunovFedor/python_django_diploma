from rolepermissions.roles import AbstractUserRole


# TODO: баг. Не заполняется auth_group_permissions. Поэтому приходится через админку его заполнять
class Client(AbstractUserRole):
    """
    Обычны клиент магазина
    """
    available_permissions = {
        'add_cart_item': True,
        'top_up_balance': True,
        'make_an_order': True,
        'account_view': True,
    }


class Moderator(AbstractUserRole):
    """
    Модерирует посты
    """
    available_permissions = {
        'top_up_balance': False,
        'make_an_order': False
    }


class SystemAdmin(AbstractUserRole):
    available_permissions = {
        'drop_tables': True,
    }