class LinksType extends Array {
  constructor(...args) {
    super(...args);
  }
  static fromDatabase(value) {
    if (!value) {
      return new LinksType();
    }

    const links = JSON.parse(value).map((item) => ({
      rel: item.rel,
      href: item.href,
      type: item.type,
      title: item.title,
    }));
    console.log(value);
    return new LinksType(links);
  }

  static toDatabase(value) {
    console.log(value)
    return JSON.stringify(value.map((item) => ({
      rel: item.rel,
      href: item.href,
      type: item.type,
      title: item.title
    })));
  }
}

export default LinksType;
