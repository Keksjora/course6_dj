from django import forms

from blog.models import Blog


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        exclude = ["count_of_views"]

    def __init__(self, *args, **kwargs):
        super(BlogModelForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите заголовок",
            }  # Добавление CSS-класса для стилизации поля
        )  # Текст подсказки внутри поля

        self.fields["content"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите контент"}
        )

        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("title")
        description = cleaned_data.get("content")

        if name.lower() and description.lower() in [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]:
            self.add_error("title", "запрещенное слово")
            self.add_error("content", "запрещенное слово")

    def clean_image(self):
        cleaned_data = super().clean()
        image = cleaned_data.get("image")

        if image.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Размер файла не должен превышать 5 МБ.")

        if image.name.endswith(("jpg", "jpeg", "png")):
            raise forms.ValidationError(
                "Недопустимый формат файла. Загрузите JPEG или PNG."
            )

        return image
