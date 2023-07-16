from dataclasses import dataclass


class InvalidCoordinates(Exception):
    pass


@dataclass
class Annotation:
    dish: str
    x: int
    y: int
    w: int
    h: int


class Image:
    def __init__(
        self,
        _id: int,
        url: str,
        width: int,
        height: int,
    ) -> None:
        self.id = _id
        self.url = url
        self.width = width
        self.height = height
        self.annotations: list[Annotation]

    def annotate(self, annotations: list[Annotation]) -> None:
        for ann in annotations:
            if not self.can_annotate(ann):
                raise InvalidCoordinates(f"Annotation {ann} has invalid coordinates.")
        self.annotations = annotations

    def can_annotate(self, ann: Annotation) -> bool:
        return ann.x + ann.w < self.width and ann.y + ann.h < self.height
