import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (currency instanceof Currency) {
      this._amount = amount;
      this._currency = currency;
    } else {
      throw new Error('Invalid currency object');
    }
  }

  get amount() {
    return this._amount;
  }

  set amount(newAmount) {
    this._amount = newAmount;
  }

  get currency() {
    return this._currency;
  }

  set currency(newCurrency) {
    if (newCurrency instanceof Currency) {
      this._currency = newCurrency;
    } else {
      throw new Error('Invalid currency object');
    }
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency} (${this._currency.code})`;
  }

  static convertCurrency(amount, conversionRate) {
    return amount * conversionRate;
  }
}
