---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---



**资源介绍**

课程资源为选课学生对公开发表论文或研究的介绍和述评，使用者应充分尊重原文和述评同学的智力成果。对原文进行引用请按规范标注引文；同学的述评和文献梳理成果仅供内部学习参考，如有引用或公开，需主动联系并经本人同意。

**资源列表**

| 学期 | 任课老师 |
| :-: | :-: |{% for semester_hash in site.data.semesters %}{% assign semester = semester_hash[1] %}
| [{{ semester.semester_name }}](/semester/{{ semester_hash[0] }}.html) | {{ semester.instructors }} |{% endfor %}



