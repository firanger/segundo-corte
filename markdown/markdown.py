
import re
BOLD_RE = re.compile(r"__(.*?)__")
ITALICS_RE = re.compile(r"_(.*?)_")
HEADER_RE = re.compile(r"(#+) (.*)")
LIST_RE = re.compile(r"\* (.*)")
def parse(markdown: str) -> str:

    result = []
    for line in markdown.splitlines():
        # expand inline bold tags
        line = BOLD_RE.sub(r"<strong>\1</strong>", line)
        # expand inline italics tags
        line = ITALICS_RE.sub(r"<em>\1</em>", line)
        # line may be a header item or a list item
        is_header = HEADER_RE.match(line)
        is_list = LIST_RE.match(line)
        # a header is not itself a paragraph
        if is_header:
            result.append("<h{0}>{1}</h{0}>".format(len(is_header.group(1)),
                                                    is_header.group(2)))
        # neither is any part of a list
        elif is_list:
            # we may be appending to an existing list
            if result and result[-1] == "</ul>":
                result.pop()
            # or starting a new one
            else:
                result.append("<ul>")
            result.extend(["<li>" + is_list.group(1) + "</li>", "</ul>"])
        # everything else is a paragraph
        else:
            result.append("<p>" + line + "</p>")
    return "".join(result)
