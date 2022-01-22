# Done: learn the yml read
# Pick: learn the jekyll generate the dynamic according to the yaml
# http://jekyllcn.com/docs/datafiles/

# use layout dynamic generate the page with yaml
# these is no support for dynamic generated post with yaml config
# require package pyyaml
#%%
import yaml
import os

yaml_base_path = "../_data/semesters"
yaml_list = os.listdir(yaml_base_path)
#%%
for yaml_file_name in yaml_list:
    with open(f"{yaml_base_path}/{yaml_file_name}", "r") as stream:
        yaml_dict = yaml.safe_load(stream)
    # yaml_dict
    # generate the md in the semester folder
    md_name = yaml_file_name.replace("yml", "md")
    template_str = f"""---
    layout: page
    ---

    **{yaml_dict["semester_name"]}**

    | 主题与浏览页面 | 论文链接 | 学生姓名 | PPT链接 | 课程所属教师 | 其他材料 |
    | :-: | :-: | :-: | :-: | :-: | :-: |
    """
    raw_base_path = (
        "https://github.com/RucStatReading/RucStatReading.github.io/raw/main/"
    )
    for piece in yaml_dict["pieces"]:
        name = piece["name"]
        title = piece["title"]
        instructor = piece["instructor"]
        page_link = "/paper/" + str(piece["date"]).replace("-", "/") + f"/{ name }.html"
        if piece["survey_pdf"] != "None":
            survey_pdf_link = (
                "[github_raw](" + raw_base_path + piece["survey_pdf"] + ")"
            )
        else:
            survey_pdf_link = "暂无"
        if piece["presentation"] != "None":
            presentation_link = (
                "[github_raw](" + raw_base_path + piece["presentation"] + ")"
            )
        else:
            presentation_link = "暂无"
        if piece["baiducloudlink"] != "None":
            baiducloudlink = piece["baiducloudlink"]
            baiducloudtoken = piece["baiducloudtoken"]
            bdshare = f"[提取码:{baiducloudtoken}]({baiducloudlink})"
        else:
            bdshare = "暂无"
        one_line_str = f"| [{title}]({page_link}) | {survey_pdf_link} | {name} | {presentation_link} | {instructor} | {bdshare} |\n"
        template_str += one_line_str
        single_template_str = f"""---
    layout: post
    title:  "{piece["title"]}"
    date:   {piece["date"]} 17:29:42 +0800
    categories: paper
    ---

    """
        single_template_str += '{% pdf "/' + piece["survey_pdf"] + '" %}\n\n'
        if piece["presentation"].split(".")[-1] == "pdf":
            single_template_str += '{% pdf "/' + piece["presentation"] + '" %}\n\n'
        else:
            single_template_str += (
                '{% pdf "' + raw_base_path + piece["presentation"] + '" %}\n\n'
            )
        with open(f"../_posts/" + str(piece["date"]) + f"-{ name }.md", "w") as f:
            f.write(single_template_str)
        # print(single_template_str)
    semester_file_name = yaml_file_name.replace("yml", "md")
    with open(f"../semester/{semester_file_name}", "w") as f:
        f.write(template_str)
    # print(template_str)

#%%
