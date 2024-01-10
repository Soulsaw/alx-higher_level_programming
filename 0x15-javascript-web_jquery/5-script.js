$('DIV#add_item').on('click', () => {
  $('UL.my_list').add('<li>Item</li>').appendTo('UL.my_list');
});
