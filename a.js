function fetchAndDownload() {
    console.log("开始执行")
    document.querySelector("[data-log-value='右侧按钮']").click();
    const col1 = ["二级类目"]
        , col2 = ["TGI"]
        , col3 = ["完播数"];
    for (let row_data of document.getElementsByClassName("byted-table-column byted-table-row")) {
        if (row_data.getElementsByClassName("byted-table-cell byted-table-cell-body byted-table-cell-first")[0].textContent !== "") {
            col1.push(row_data.getElementsByClassName("byted-table-cell byted-table-cell-body byted-table-cell-first")[0].textContent)
            col2.push(row_data.getElementsByClassName("byted-table-cell byted-table-cell-body")[1].textContent)
            col3.push(row_data.getElementsByClassName("byted-table-cell byted-table-cell-body byted-table-cell-last")[0].textContent)
        }
    }

    const results = [];
    data = {
        "col1": col1,
        "col2": col2,
        "col3": col3,
    }
    data.col1.forEach((val, idx) => {
        if (idx === 0) {
            // 第一行是表头，不需要处理
            results.push(val);
        } else {
            // 把当前行的三个值组合到一起
            results.push(`${val}|${data.col2[idx]}|${data.col3[idx]}`);
        }
    });

    // 最终结果
    console.log(results.join("\n"));

    return
}
// 创建一个新的按钮元素
const copyDataBtn = document.createElement('div');
copyDataBtn.classList.add('index__iconContainer--jt9As', 'index__iconWrap--ua1gA');
copyDataBtn.id = 'copyDataBtn';

// 创建按钮元素内部的HTML内容（图标和标题）
const btnContent = `
    <div elementtiming="element-timing" data-immersive-translate-effect="1">
        <img alt="" src="http://file.modubus.com/otherpros/mediabook/PC/logo.png" elementtiming="element-timing" style="width: 24px;" data-immersive-translate-effect="1">
        <div class="index__text--OgJxz" elementtiming="element-timing" data-immersive-translate-effect="1">
            <font data-immersive-translate-effect="1">复制数据</font>
        </div>
    </div>
`;

// 将HTML内容插入到新的按钮元素中
copyDataBtn.innerHTML = btnContent;

// 找到原来的按钮容器，将新按钮插入到该容器的前面
const buttonGroup = document.getElementById('bottom_btn_group');
buttonGroup.insertBefore(copyDataBtn, buttonGroup.firstChild);

// 绑定点击事件，调用函数fetchAndDownload
copyDataBtn.addEventListener('click', fetchAndDownload);

const xpath1 = "/html[@class='no-touch']/body/div[@id='root']/div[@class='index__main--v6QZW']/section[@class='byted-layout byted-layout-has-aside byted-layout-light']/section[@id='contentLayout']/div[@id='modern_sub_app_container_content']/div[@id='garfish_app_for_content_gtn5brpu']/div/div[2]/div/div[7]/div/div[@class='byted-loading byted-loading-block']/div[2]/div[@class='index__wordTable--MUf4_']/div/div[@class='byted-loading byted-loading-block']/div[@class='index__tableWrapper--RbUKV']/div[@class='byted-table']/div[@class='byted-loading byted-loading-block']/div[@class='byted-table-container byted-table-container-row']/div[@class='byted-table-scroller']/div[@class='byted-table-body']/div[@class='byted-table-column byted-table-row index__selectedRow--sFT4i']/div[@class='byted-table-column-visible']/div[@class='byted-table-column-scroller']/div[@class='byted-table-cell byted-table-cell-body byted-table-cell-first']"

const html = document.body.innerHTML;
// 获取HTML页面
const result = document.evaluate(xpath1, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
// 执行XPath
console.log(result)
const data = [];
for (let i = 0; i < result.snapshotLength; i++) {
    const item = result.snapshotItem(i);
    data.push(item.textContent.trim());
    // 提取元素的文本内容，并去除头尾空格
}

console.log(data);
// 输出提取的数据
