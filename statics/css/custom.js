document.addEventListener("DOMContentLoaded", function () {
  // 检查localStorage是否已设置
  var isPopupClosed = localStorage.getItem("popupClosed");
  var currentDate = new Date();
  if (isPopupClosed) {
    var closedDate = new Date(isPopupClosed);
    if (currentDate - closedDate < 86400000) {
      return;
    }
  }

  var popup = document.createElement("div");
  popup.id = "my-popup";

  // 创建关闭按钮
  var closeButton = document.createElement("span");
  closeButton.textContent = "X";
  closeButton.className = "close-btn";
  popup.appendChild(closeButton);

  // 创建链接元素
  var link = document.createElement("a");
  link.href = "https://www.fre123.com/weekly?from=weekly";
  link.textContent = "🔥 老胡精选周刊大全>>>";
  link.target = "_blank";
  popup.appendChild(link);
  document.body.appendChild(popup);

  setTimeout(function () {
    popup.classList.add("show");
  }, 500);

  //关闭按钮事件
  closeButton.addEventListener("click", function (event) {
    event.stopPropagation(); // 阻止事件冒泡
    popup.classList.remove("show");
    localStorage.setItem("popupClosed", new Date().toISOString()); // 设置关闭时间
  });
});
