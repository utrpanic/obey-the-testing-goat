from django import forms
from django.core.exceptions import ValidationError
from lists.models import Item

DUPLICATE_ITEM_ERROR = '이미 리스트에 해당 아이템이 있습니다'
EMPTY_LIST_ERROR = '빈 아이템을 등록할 수 없습니다'

class ItemForm(forms.models.ModelForm):

    # Input 태그에 required 필드 때문에
    # 빈 값이 아예 입력이 안됨. form_action이 불리질 않는다.
    # 그렇다고 required를 꺼버리면
    # Form validation만 하고 저장해버리기 때문에
    # DB에 에러 없이 저장해버림.
    # form.is_valid()에 대해 더 알게 되면 개선하기.
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['text'].required = False

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': '작업 아이템 입력',
                'class': 'form-control input-lg',
            }),
        }
        error_messages = {
            'text': { 'required': EMPTY_LIST_ERROR }
        }

    def save(self, for_list):
        self.instance.list = for_list
        return super().save()

class ExistingListItemForm(ItemForm):

    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list

    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)