import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import select
from esphome.const import CONF_ID, CONF_OPTIMISTIC

from .. import CONF_PIPSOLAR_ID, PIPSOLAR_COMPONENT_SCHEMA, pipsolar_ns
from ..const import CONF_CHARGER_SOURCE_PRIORITY, CONF_OUTPUT_SOURCE_PRIORITY

DEPENDENCIES = ["uart"]
CODEOWNERS = ["@andreashergert1984"]
AUTO_LOAD = ["binary_sensor", "text_sensor", "sensor", "switch", "output", "select"]
MULTI_CONF = True

CONF_PIPSOLAR_ID = "pipsolar_id"
CONF_OPTIONSMAP = "optionsmap"
CONF_STATUSMAP = "statusmap"

CONF_OUTPUT_SOURCE_PRIORITY = "output_source_priority"
CONF_CHARGER_SOURCE_PRIORITY = "charger_source_priority"
CONF_CHARGING_DISCHARGING_CONTROL = "charging_discharging_control"
CONF_CURRENT_MAX_CHARGING_CURRENT = "current_max_charging_current"
CONF_CURRENT_MAX_AC_CHARGING_CURRENT = "current_max_ac_charging_current"
pipsolar_ns = cg.esphome_ns.namespace("pipsolar")
PipsolarComponent = pipsolar_ns.class_("Pipsolar", cg.Component)

TYPES = {
    CONF_OUTPUT_SOURCE_PRIORITY: ("POP00", None),
    CONF_CHARGER_SOURCE_PRIORITY: ("PCP03", None),
    CONF_CHARGING_DISCHARGING_CONTROL: ("PBATCD111", None),
    CONF_CURRENT_MAX_CHARGING_CURRENT: ("MCHGC010", None),
    CONF_CURRENT_MAX_AC_CHARGING_CURRENT: ("MUCHGC0002", None),
}
PIPSOLAR_COMPONENT_SCHEMA = cv.Schema(
    {
        cv.Required(CONF_PIPSOLAR_ID): cv.use_id(PipsolarComponent),
    }
)

CONFIG_SCHEMA = cv.All(
    cv.Schema({cv.GenerateID(): cv.declare_id(PipsolarComponent)})
    .extend(cv.polling_component_schema("1s"))
    .extend(uart.UART_DEVICE_SCHEMA)
)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield uart.register_uart_device(var, config)
