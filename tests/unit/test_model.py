import pytest

from annotation.domain import model


def test_can_add_annotation_to_image():
    img = model.Image(_id=1, url="blabla", width=1920, height=1080)
    ann = model.Annotation(dish="potatoes", x=100, y=150, w=300, h=300)
    img.annotate([ann])
    assert len(img.annotations) == 1
    assert img.annotations[0] == ann


def test_cannot_annotate_img_with_bigger_bbox():
    img = model.Image(_id=1, url="blabla", width=1920, height=1080)
    ann = model.Annotation(dish="potatoes", x=1000, y=1500, w=3000, h=3000)
    with pytest.raises(model.InvalidCoordinates):
        img.annotate([ann])
