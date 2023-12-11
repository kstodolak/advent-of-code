module.exports = function () {
  Object.defineProperties(Array.prototype, {
    maxIndex: {
      value: function () {
        return this.indexOf(this.max());
      },
    },
    max: {
      value: function () {
        if (!this.length) return null;
        return [...this].sort((a, b) => b - a)[0];
      }
    },
    minIndex: {
      value: function () {
        return this.indexOf(this.min());
      },
    },
    min: {
      value: function () {
        if (!this.length) return null;
        return [...this].sort((a, b) => a - b)[0];
      }
    },
    midIndex: {
      value: function () {
        if (!this.length) return -1;
        if (this.length === 1) return 1;

        return Math.floor(this.length / 2);
      }
    },
    median: {
      value: function () {
        if (!this.length) return null;
        if (this.length === 1) return this[1];

        const sorted = [...this].sort((a, b) => a - b);
        const midIndex = this.midIndex();
        return !(this.length % 2)
          ? (sorted[midIndex - 1] + sorted[midIndex]) / 2
          : sorted[midIndex];
      }
    },
    sum: {
      value: function () {
        return this.reduce((sum, a) => sum += a, 0);
      }
    },
    mean: {
      value: function () {
        return this.sum() / this.length;
      }
    },
    count: {
      value: function (cb) {
        return this.filter(typeof cb === 'function' ? cb : (el) => el == cb).length;
      }
    },
    freqCountMap: {
      value: function () {
        return [...this].uniq().map(el => [el, this.count(el)]).sortDesc(1);
      }
    },
    uniq: {
      value: function () {
        return this.filter((val, i, self) => self.indexOf(val) === i);
      }
    },
    sortAsc: {
      value: function (index) {
        return [...this].sort((a, b) => index !== undefined ? (a[index] - b[index]) : (a - b));
      }
    },
    sortDesc: {
      value: function (index) {
        return [...this].sort((a, b) => index !== undefined ? (b[index] - a[index]) : (b - a));
      }
    }
  });
};
