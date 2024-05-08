import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }

  set amount(newAmount) {
    this._amount = newAmount;
  }

  get amount() {
    return this._amount;
  }

  set currency(newCurrency) {
    if (!(newCurrency instanceof Currency)) throw new TypeError('Currency must be a Currency');
    this._currency = newCurrency;
  }
}
